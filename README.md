# Corel

<img src="https://github.com/yohanesnuwara/corel/assets/51282928/5403fb5c-74f7-499f-9bca-4b97eeb214cb" alt="Alt Text" width="400px">

Corel is a smart computer vision model that identifies facies and performs rock typing on core images. It is based on YOLOv8-Segmentation model that is trained to classify different facies and sedimentary features from core images. The facies include:
* Bioturbated mudstone/sandstone
* Massive mudstone/sandstone
* Parallel-laminated mudstone/sandstone
* Cross-bedded/graded-bedded sandstone
* Current-rippled sandstone
* Conglomerate
* Fissile shale
* Heterolithic

### 🤖 Try Corel --> [HERE](https://github.com/yohanesnuwara/corel/blob/main/notebooks/Corel.ipynb) <-- Upload your own core image (or use example image in folder [core_images](https://github.com/yohanesnuwara/corel/tree/main/core_images))

### Result

The following is example of result of Corel facies classification on core image which can accurately make segmentation for every sedimentary changes such as parallel-laminated sandstone, massive sandstone, etc. 

<img src="https://github.com/yohanesnuwara/corel/assets/51282928/1ced32ba-bb67-4f2b-af91-ca70ab7d8a6d" alt="Alt Text" width="500px">

<img src="https://github.com/yohanesnuwara/corel/assets/51282928/15cbb7cb-4bf4-4aa4-912c-5603895aba7f" alt="Alt Text" width="300px">

### Engineering

Corel uses simple data architecture as follows. Corel model is stored in Azure Storage which is then deployed when detection is run on images. 

<img src="https://github.com/yohanesnuwara/corel/assets/51282928/a50197d0-ac4c-42e3-861b-fa91c9a6cbce" alt="Alt Text" width="500px">

### Training

The medium-sized YOLOv8-Segmentation model is trained with tuned hyperparameters using Ray Tune algorithm. The fitness after 14 iterations is 0.64, which gives the hyperparameter that we use for training Corel model.

<img src="https://github.com/yohanesnuwara/corel/assets/51282928/e1bb3131-154b-401a-818f-95cdca8f9463" alt="Alt Text" width="500px">

Current average F1-score for all facies is 0.654. The matrix confusion is as follows

<img src="https://github.com/yohanesnuwara/corel/assets/51282928/eb2b10fd-e92f-4522-8125-7b7eea1ffd03" alt="Alt Text" width="700px">
