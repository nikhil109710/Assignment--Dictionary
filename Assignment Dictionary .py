#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create an empty dictionary
student_data = {}


# In[2]:


# Add the key values
student_data["name"] = "John"
student_data["age"] = 20
student_data["major"] = "Computer Science"


# In[3]:


# Print the student_data
print(student_data)


# In[5]:


# Access and print the age 
print(student_data["age"])


# In[6]:


# Update the major
student_data["major"] = "Data Science"


# In[7]:


# Add the key value 
student_data["GPA"] = 3.68


# In[10]:


# Print all the values in student_data
print(student_data)


# In[12]:


# Check if grade exists or not and print the result
print("grade" in student_data)


# In[13]:


# Delete the key value
del student_data["age"]


# In[ ]:




