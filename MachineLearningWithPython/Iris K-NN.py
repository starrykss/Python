#!/usr/bin/env python
# coding: utf-8

# # Iris K-NN

# In[1]:


from sklearn.datasets import load_iris
iris_dataset = load_iris()


# # 1. 데이터 적재

# In[2]:


print("iris_dataset의 키:\n", iris_dataset.keys())


# In[3]:


# 데이터에 대한 설명
print(iris_dataset['DESCR'][:193] + "\n...")


# In[4]:


print("타깃의 이름:", iris_dataset['target_names'])


# In[5]:


print("특성의 이름:", iris_dataset['feature_names'])


# In[6]:


print("데이터의 타입:", type(iris_dataset['data']))


# In[7]:


print("데이터의 크기:", iris_dataset['data'].shape)


# In[8]:


print("데이터의 처음 다섯 행:\n", iris_dataset['data'][:5])


# In[9]:


print("target의 타입:", type(iris_dataset['target']))


# In[10]:


print("target의 크기:", iris_dataset['target'].shape)


# In[11]:


print("타깃:\n", iris_dataset['target'])


# # 2. 성과 측정: 훈련데이터와 테스트 데이터

# In[16]:


from sklearn.model_selection import train_test_split

# train : test = 0.75 : 0.25
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)


# In[17]:


print("X_train 크기:", X_train.shape)
print("y_train 크기:", y_train.shape)


# In[18]:


print("X_test 크기:", X_test.shape)
print("y_test 크기:", y_test.shape)


# # 3. 가장 먼저 할일 : 데이터 살펴보기

# In[27]:


import pandas as pd
from preamble import *

# X_train 데이터를 사용해서 데이터프레임을 만듭니다.
# 열의 이름은 iris_dataset, feature_names에 있는 문자열을 사용합니다.
iris_dataframe = pd.DataFrame(X_train, columns = iris_dataset.feature_names)

# 데이터프레임을 사용해 y_train에 따라 색으로 구분된 산점도 행렬을 만듭니다.
pd.plotting.scatter_matrix(iris_dataframe, c = y_train, figsize = (15, 15), marker = 'o', hist_kwds = {'bins' : 20}, s = 60, alpha = 8, cmap = mglearn.cm3)


# # 4. 첫번째 머신러닝 모델 : K-최근접 이웃 알고리즘

# In[30]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)


# In[33]:


knn.fit(X_train, y_train)


# # 5. 예측 및 모델 평가하기

# In[35]:


X_new = np.array([[5, 2.0, 1, 0.2]])
print("X_new.shape:", X_new.shape)


# In[36]:


prediction = knn.predict(X_new)
print("예측:", prediction)
print("예측한 타깃의 이름:", iris_dataset['target_names'][prediction])


# In[38]:


y_pred = knn.predict(X_test)
print("테스트 세트에 대한 예측값:\n", y_pred)


# In[44]:


print("테스트 세트의 정확도: {:.2f}".format(np.mean(y_pred == y_test)))


# In[45]:


print("테스트 세트의 정확도: {:.2f}".format(knn.score(X_test, y_test)))


# # 6. 요약

# In[46]:


X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)

knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, y_train)

print("테스트 세트의 정확도: {:.2f}".format(knn.score(X_test, y_test)))


# In[ ]:




