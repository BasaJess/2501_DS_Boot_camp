Neue fische School and Pool for Digital Talent 
___
# Data Science Boot Camp

 **26 February 2025 / Online Session** 

### INSTRUCTOR

Parvin Shafiri (Senior Coach DS)

### ATTENDEES

Annete Manntschke, Aylin Hanne, Eva Schmidt, Jesus Gonzalez, Jonas Schors, Katharina Baumgarter, Lida Shamsafar, Maren Bormann, Maria Berger, Parya Tavakoli-Therani, Simon Cornevin, Tim Weiand, Utku Oezkan

## TOPICS : KNN AND DISTANCE METRICS

### **Summary:**

1. Recap on General Concepts: In <strong>supervised learning</strong>, algorithms are trained using labeled datasets, meaning each input comes with a corresponding correct output. **Unsupervised learning** involves algorithms analyzing unlabeled data to identify hidden patterns or intrinsic structures without external guidance.

2. The k-Nearest Neighbors (**k-NN**) algorithm is a **straightforward, non-parametric** supervised learning method used for both **classification** and **regression** tasks. It operates on the principle that data points with similar features are likely to have similar outcomes. In essence, k-NN classifies a new data point based on the majority class among its 'k' closest neighbors in the feature space.

3. **Distance Metrics**: There are different ways of quantifying Distance, we explored: Euclidian, Manhattan, Minkowsi and Cosine Similarity.Selecting the appropriate distance metric is crucial for the performance of algorithms.

---

<div align="center">

| <img src="Supervised_learning.png" alt="Spervised Learning" width="300" height="300"> |<img src="Distance_metrics.png" alt="Spervised Learning" width="300" height="300">  |
| :-----: | :-----: |
| `Supervised Learning` | `Distance Metrics` |

</div>   

# NOTES

## **Supervised vs. Unsupervised Learning**
<div align="center">

| Supervised | Unsupervised | 
| :---------------: | :---------------: | 
| Requires labeled Data   | Works with unlabeled Data   | 
| Predicts outcomes for new Data based on learned patterns |Aims to uncover hidden patterns|
| Used where historical data with known outcomes is available|Seeks to understand the underlying relationships within the data, making it useful for exploratory analysis|
| Linear regression, support vector machines, and neural networks | K-means clustering, hierarchical clustering, and principal component analysis   |
| Classifying E-mails as Spam or not, Image recognition (Cat or Dog), Forecasting future sales|Customer Segmentation (purchasing behaviour), Anomaly Detection (unusual data points, fraud detection), Dimensionality Reduction (reduce the number of variables in data to make visualization easier )| 

</div>


<style>
  table {
    border-collapse: collapse;
    width: 100%;
  }
  th, td {
    border: 1px solid black;
    padding: 8px;
    text-align: left;
  }
</style>


# KNN
### Paradigm
- Birds of a feather flock together
- Sampe principle as Kitchen Table vs Fridge
- Or Computer Memory Cache
- It is still a Supervised algorithm

### Why KNN
- Despite being simple
   - Good for Classification (handwriting of numeric characters, or satellite imagery)
   - It solves also regression problems

### Characteristics
 - Non parametric
 - Input (Features, Target, Hyperparameters)
   - Nr of Neighbors, K
   - Distance Metric
   - Weight
 - Loops through all observations
 - Calculates the distance to everyone
 - Sort and Pick the closest neighboors
 - Pick a k that does not over or under-fit

### How to measure proximity? 
 - Categorical features can be a problem
 - Which Distance? (To be detailed below)
    - Euclidian
    - Manhatann
    - Minkowski
    - Cosine 

<img src="knn_animation.gif" alt="Spervised Learning" width="500" height="500">

# DISTANCE METRICS

Not all the distances are the same

- Evolution? 
  - Minkowski
  - Euclidian
  - Manhattan
  - But then Cosine
- Do not forget Scaling or not (David vs Goliath)


# EXTERNAL LINKS AND FURTHER INFO

here some cool stuff
