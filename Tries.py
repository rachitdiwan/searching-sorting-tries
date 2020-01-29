#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[8]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.dict = {}

    def insert(self, char):
        if char in self.dict:
            return
        self.dict[char] = TrieNode()
    
    def get_dict(self):
        return self.dict
    
    def get_node(self, value):
        if value not in self.dict:
            return None
        return self.dict[value]
        
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        cur_node = self.root
        for val in word:
            cur_node.insert(val)
            cur_node = cur_node.get_node(val)

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        cur_node = self.root
        for val in prefix:
            if cur_node is None:
                return None
            cur_node = cur_node.get_node(val)
        return cur_node


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[30]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.dict = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char in self.dict:
            return
        self.dict[char] = TrieNode() 
        
    def get_dict(self):
        return self.dict
    
    def get_node(self, value):
        if value not in self.dict:
            return None
        return self.dict[value]

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        if len(self.dict) == 0:
            return suffix
        suf_list = []
        for val in self.dict:
            pro = suffix + val
            suf_list.append(self.dict[val].suffixes(pro))
        new_list = []
        for value in suf_list:
            if type(value) == list:
                for val in value:
                    new_list.append(val)
            else:
                new_list.append(value)
        return new_list
                


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[31]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[32]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:




