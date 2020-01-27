
"""
Title: Dimensionality Reduction on MNIST dataset using PCA, LDA, and TSNE

@author: Saeed Mohajeryami, PhD

"""
#import basic libraries
import numpy as np
import pandas as pd

# import visualization libraries
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import seaborn as sns
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#%matplotlib inline

# Import the 3 dimensionality reduction methods
from sklearn.manifold import TSNE #unsupervised, nonlinear
from sklearn.decomposition import PCA #unsupervised, linear
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA #supervised, linear

# tools
from sklearn.preprocessing import StandardScaler

## -------------------- dataset --------------------------------
train = pd.read_csv('train.csv')
X = train.iloc[:,1:].values
y = train.iloc[:,0:1].values
Target = np.ravel(train.iloc[:,0:1].values)   # same as y

# Standardize the data
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

## -------------------- PCA --------------------------------
# Calculating Eigenvectors and eigenvalues of Cov matirx
mean_vec = np.mean(X_std, axis=0)
cov_mat = np.cov(X_std.T)
eig_vals, eig_vecs = np.linalg.eig(cov_mat)
# Create a list of (eigenvalue, eigenvector) tuples
eig_pairs = [ (np.abs(eig_vals[i]),eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the eigenvalue, eigenvector pair from high to low
eig_pairs.sort(key = lambda x: x[0], reverse= True)

# Calculation of Explained Variance from the eigenvalues
tot = sum(eig_vals)
var_exp = [(i/tot)*100 for i in sorted(eig_vals, reverse=True)] # Individual explained variance
cum_var_exp = np.cumsum(var_exp) # Cumulative explained variance

# As we can see, out of our 784 features or columns approximately 90% of the
# Explained Variance can be described by using just over 200 over features.
# So if one wanted to implement a PCA on this, extracting the top 200 features
# would be a very logical choice as they already account for the majority of
# the data.

# Using sklearn PCA
pca = PCA(n_components=30)
pca = pca.fit(X_std)
eigenvalues = pca.components_
X_std_30 = pca.transform(X_std)

n_row = 4
n_col = 4

# Plot the first 16 eignenvalues
plt.figure(figsize=(13,12))
for i in list(range(n_row * n_col)):
    offset =0
    plt.subplot(n_row, n_col, i + 1)
    plt.imshow(eigenvalues[i].reshape(28,28), cmap='jet')
    title_text = 'Eigenvalue ' + str(i + 1)
    plt.title(title_text, size=6.5)
    plt.xticks(())
    plt.yticks(())
plt.show()

# plot some of the numbers
plt.figure(figsize=(14,12))
for digit_num in range(0,70):
    plt.subplot(7,10,digit_num+1)
    grid_data = train.iloc[:,1:].iloc[digit_num].as_matrix().reshape(28,28)  # reshape from 1d to 2d pixel array
    plt.imshow(grid_data, interpolation = "none", cmap = "afmhot")
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()

## ------------------------- visualization ---------------------------
trace0 = go.Scatter(
    x = X_std_30[:,0],  # first principal component
    y = X_std_30[:,1],  # second principal component
#     name = Target,
#     hoveron = Target,
    mode = 'markers',
    text = Target,
    showlegend = False,
    marker = dict(
        size = 8,
        color = Target,
        colorscale ='Jet',
        showscale = False,
        line = dict(
            width = 2,
            color = 'rgb(255, 255, 255)'
        ),
        opacity = 0.8
    )
)
data = [trace0]

layout = go.Layout(
    title= 'Principal Component Analysis (PCA)',
    hovermode= 'closest',
    xaxis= dict(
         title= 'First Principal Component',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= 'Second Principal Component',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= True
)


fig = dict(data=data, layout=layout)
py.plot(fig, filename='pca_styled-scatter.html')


## ------------------------- LDA ------------------------------------
lda = LDA(n_components=5)
# Taking in as second argument the Target as labels
X_LDA_2D = lda.fit_transform(X_std,np.ravel(y))

# Using the Plotly library again
traceLDA = go.Scatter(
    x = X_LDA_2D[:,0],
    y = X_LDA_2D[:,1],
#     name = Target,
#     hoveron = Target,
    mode = 'markers',
    text = Target,
    showlegend = True,
    marker = dict(
        size = 8,
        color = Target,
        colorscale ='Jet',
        showscale = False,
        line = dict(
            width = 2,
            color = 'rgb(255, 255, 255)'
        ),
        opacity = 0.8
    )
)

data = [traceLDA]

layout = go.Layout(
    title= 'Linear Discriminant Analysis (LDA)',
    hovermode= 'closest',
    xaxis= dict(
         title= 'First Linear Discriminant',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= 'Second Linear Discriminant',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False
)

fig = dict(data=data, layout=layout)
py.plot(fig, filename='lda_styled-scatter.html')

## ------------------------- TSNE ------------------------------------
tsne = TSNE(n_components=2)
tsne_results = tsne.fit_transform(X_std)

traceTSNE = go.Scatter(
    x = tsne_results[:,0],
    y = tsne_results[:,1],
    name = Target,
     hoveron = Target,
    mode = 'markers',
    text = Target,
    showlegend = True,
    marker = dict(
        size = 8,
        color = Target,
        colorscale ='Jet',
        showscale = False,
        line = dict(
            width = 2,
            color = 'rgb(255, 255, 255)'
        ),
        opacity = 0.8
    )
)
data = [traceTSNE]

layout = dict(title = 'TSNE (T-Distributed Stochastic Neighbour Embedding)',
              hovermode= 'closest',
              yaxis = dict(zeroline = False),
              xaxis = dict(zeroline = False),
              showlegend= False,

             )

fig = dict(data=data, layout=layout)
py.plot(fig, filename='tsne_styled-scatter.html')

#From the t-SNE scatter plot the first thing that strikes is that clusters 
# ( and even subclusters ) are very well defined and segregated resulting
# in Jackson-Pollock like Modern Art visuals, even more so than the PCA and
# LDA methods. This ability to provide very good cluster visualisations can
# be boiled down to the topology-preserving attributes of the algorithm. 
# However t-SNE is not without its drawbacks. Multiple local minima may occur
# as the algorithm is identifying clusters/sub-clusters and this can be evinced
# from the scatter plot, where we can see that clusters of the same colour 
# exist as 2 sub-clusters in different areas of the plot.