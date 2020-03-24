#!/usr/bin/env python
# coding: utf-8

# In[7]:


# default 설정
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[29]:


np.random.seed(1)
x = np.arange(10)     # 0~9 사이 랜덤 수
y = np.random.randn(10) # 0~1 사이 랜덤 수
print(x)
print(y)


# In[32]:


# 그래프 표시
plt.plot(x, y)  # 꺾은선 그래프를 등록
plt.show()


# In[ ]:


## EX1) f(x) = 2x + 3


# In[36]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[41]:


def f(x):
    return 2 * x + 3


# In[42]:


x = np.arange(-5, 5, 1)
y = f(x)
print(x, y)


# In[40]:


plt.plot(x, y)
plt.grid(True)   # Grid 추가
plt.show()


# In[90]:


## EX2) f(x) = (x-2)x(x+2)


# In[45]:


def f(x):
    return (x - 2) * x * (x + 2)


# In[46]:


print(f(1))
print(f(np.array([1, 2, 3])))


# In[52]:


x = np.arange(-3, 3.5, 0.5)   # 0.5 간격으로 -3~3까지의 숫자 생성
print(x)


# In[61]:


x = np.linspace(-3, 3, 10)   # -3~3까지의 숫자 생성. 마지막 인자 값이 클수록 곡선이 완만해짐.
print(np.round(x, 2))        # 소수점 둘째자리까지 출력
y = f(x)


# In[62]:


plt.plot(x, y)
plt.show()


# In[63]:


## EX3) f(x) = ax^3 + bx^2 + cx + d


# In[ ]:


# 싱글 그래프


# In[91]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[92]:


def f(a, b, c, d, x):
    return (a * x ** 3) + (b * x ** 2) + (c * x) + d


# In[93]:


x = np.linspace(-3, 3, 100)

a = 1
b = 2
c = 3
d = 4

y = f(a, b, c, d, x)


# In[94]:


plt.plot(x, y, color='orange')   # 곡선 색깔 : Orange
plt.grid(True)                   # Grid 생성
plt.show()


# In[95]:


# 멀티 그래프


# In[96]:


# 임의의 a, b, c, d 값 설정
l = [1, 2, 3, 4]
m = [4, 3, 5, 1]
n = [7, 6, 2, 3]
k = [3, 8, 9, 2]

plt.subplot(2, 2, 1)
plt.plot(x, f(l[0], l[1], l[2], l[3], x), color = 'red')

plt.subplot(2, 2, 2)
plt.plot(x, f(m[0], m[1], m[2], m[3], x), color = 'green')

plt.subplot(2, 2, 3)
plt.plot(x, f(n[0], n[1], n[2], n[3], x), color = 'blue')

plt.subplot(2, 2, 4)
plt.plot(x, f(k[0], k[1], k[2], k[3], x), color = 'orange')


# In[97]:


## 이변수 함수 3차원 그래프 : f(x0, x1) = (2x0^2 + x1^2) * exp(-(2x0^2 + x1^2))


# In[101]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
get_ipython().run_line_magic('matplotlib', 'inline')


# In[104]:


def f(x0, x1):
    r = 2 * x0 ** 2 + x1 ** 2
    return r * np.exp(-r)


# In[106]:


# 임의의 값 입력
xn = 20
x0 = np.linspace(-2, 2, xn)
x1 = np.linspace(-2, 2, xn)
y = np.zeros((len(x0), len(x1)))
for i0 in range(xn):
    for i1 in range(xn):
        y[i1, i0] = f(x0[i0], x1[i1])


# In[109]:


xx0, xx1 = np.meshgrid(x0, x1)
ax = plt.subplot(1, 1, 1, projection='3d')
ax.plot_surface(xx0, xx1, y, color = 'blue', rstride = 1, cstride = 1, alpha = 0.3, edgecolor = 'black')


# In[ ]:




