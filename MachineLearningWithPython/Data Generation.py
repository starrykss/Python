#!/usr/bin/env python
# coding: utf-8

# In[3]:


from preamble import *


# # 지도학습

# ## 분류와 회귀

# ### 지도 학습 알고리즘

# #### 데이터셋 생성

# In[13]:


# 데이터셋을 만듭니다.
X, y = mglearn.datasets.make_forge()

# 산점도를 그립니다.
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["class 0", "class 1"], loc = 'best')
plt.xlabel('feature 1')
plt.ylabel('feature 2')
print('X.shape: ', X.shape)


# In[20]:


X, y = mglearn.datasets.make_wave(n_samples = 40)
plt.plot(X, y, 'o')
plt.ylim(-3, 3)
plt.xlabel("feature")
plt.ylabel("target")


# In[22]:


from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print("cancer.keys():\n", cancer.keys())


# In[23]:


print("유방암 데이터의 형태:", cancer['data'].shape)


# In[24]:


print("종양 종류", cancer['target_names'])


# In[25]:


print("종양", cancer['target'])


# In[26]:


print("클래스별 샘플 갯수:\n", 
     {n: v for n, v in zip(cancer['target_names'], np.bincount(cancer['target']))})


# In[27]:


print("특성 이름:\n", cancer['feature_names'])


# In[29]:


from sklearn.datasets import load_boston
boston = load_boston()
print("데이터의 형태:", boston.data.shape)


# In[32]:


X, y = mglearn.datasets.load_extended_boston()
print("X.shape:", X.shape)

