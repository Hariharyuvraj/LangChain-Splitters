from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """ What is the difference between supervised, unsupervised, and reinforcement learning?
 Explain overfitting and underfitting. How can they be avoided?
 What is the bias-variance tradeoff?
 Define precision, recall, F1 score, and accuracy.
 What is the difference between parametric and non-parametric models?
 Explain the difference between a generative and a discriminative model.
 What are the main steps in a machine learning project workflow?
 Explain feature scaling and normalization.
 How does a decision tree work?
 What is the difference between bagging and boosting?
 Explain the working of the k-nearest neighbors (KNN) algorithm.
 How does linear regression work?
 Explain logistic regression and its assumptions.
 How does a support vector machine (SVM) classify data?
 What is PCA, and when is it used?
 Explain how K-means clustering works.
 What is a random forest, and how does it prevent overfitting?
 Compare gradient boosting machines and XGBoost."""

# splitter making

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(chunks)

print(len(chunks))

print(type(chunks))