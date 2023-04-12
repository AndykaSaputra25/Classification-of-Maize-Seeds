# Maize Seed Classification Using Modified VGG-19 with Transfer Learning and Fine Tuning

## Introduction
Agricultural products, especially maize, are significant for cultivation in Indonesia, one of which is on the island of Madura. Maize is one of the strategic commodities besides rice. To continue to increase maize commodities, it is necessary to improve the quality of maize plants. One of the factors in improving the quality of maize comes from the seed. Maize seeds are the beginning of maize plants. Haploid maize seeds are used in the breeding process. When haploid cells are subjected to chromosome doubling, Double Haploid (DH) genotypes are formed. DH is an important technique in maize breeding, modern crop improvement in genetic programmes because it shortens the breeding period and can increase breeding efficiency. However, the selection of haploid seeds from diploids is a major problem. Classification is a way to classify haploid and diploid maize seeds. The development of computer-aided technology can help in the selection of haploid seeds. To achieve this goal, the Convolutional Neural Network (CNN) method is used to classify haploid and diploid maize seed images automatically with a transfer learning approach. Modification of Visual Geometry Group (VGG) 19 architecture with transfer learning and fine-tuning is applied for this thesis. The dataset obtained is 3000 digital images, consisting of 1230 haploid and 1770 diploid. In the research, undersampling, 5-fold cross validation, and fine-tuning techniques were used to support the success of the model. Testing scenarios were carried out using unbalanced and balanced data, as well as without fine-tuning and the application of fine-tuning. Confusion matrix is used to measure the success of the model. VGG-19 modified with transfer learning and fine-tuning gave excellent results in classifying corn seeds. Accuracy, precision, recall, f1-score, and AUC on balanced data and the application of fine-tuning are 96.83%, 95.9%, 98.87%, 97.36%, and 96.39%. Based on the experimental results, balancing the data and applying fine-tuning resulted in the best performance based on the confusion matrix of the model.

## Dataset
The complete description of dataset is given on https://www.rovile.org/datasets/haploid-and-diploid-maize-seeds-dataset/ The dataset contains 3000 images of maize seeds.
![alt text](https://github.com/AndykaSaputra25/Classification-of-Maize-Seeds/blob/master/image/dataset.jpg?raw=True)

## Architecture System
![alt text](https://github.com/AndykaSaputra25/Classification-of-Maize-Seeds/blob/master/image/arsitektur.JPG?raw=True)

## Preprocessing
Pre-processing is done to obtain good data that is easy to read by the system. Since there are imbalanced data, the data is used proportionally based on the least amount of data or undersampling on imbalanced data for research experiments. This technique adjusts the amount of data according to the least amount of data randomly in data selection. In accordance with the size of the VGG-19, the image size was changed to 224x224 pixels. The division of testing data is 20% and training 80%. The training data is further divided into 80% training and 20% validation.

## Result
#### Data is divided into three, namely training data, validation data, and testing data. To create validation data is done by using 5 fold cross validation on training data. The following is a visualisation of the model learning results.
![alt text](https://github.com/AndykaSaputra25/Classification-of-Maize-Seeds/blob/master/image/training.JPG?raw=True)

#### Below shows the result on evaluation model for each experimental results
![alt text](https://github.com/AndykaSaputra25/Classification-of-Maize-Seeds/blob/master/image/training%20evaluation.JPG?raw=True)

#### And below are the performance results of the model. Experiment-4 gives the best results. This model will be implemented in the interface programme.
![alt text](https://github.com/AndykaSaputra25/Classification-of-Maize-Seeds/blob/master/image/confusion.JPG?raw=True)
![alt text](https://github.com/AndykaSaputra25/Classification-of-Maize-Seeds/blob/master/image/perform%20model.JPG?raw=True)
![alt text](https://github.com/AndykaSaputra25/Classification-of-Maize-Seeds/blob/master/image/visualisasi.JPG?raw=True)

#### The resulting best model is used for the interface programme.
![alt text](https://github.com/AndykaSaputra25/Classification-of-Maize-Seeds/blob/master/image/interface.JPG?raw=True)
![alt text](https://github.com/AndykaSaputra25/Classification-of-Maize-Seeds/blob/master/image/predict.JPG?raw=True)
