# A Cost-Efficient Online Voting System Based on Facial Recognition

The conventional voting system necessitates a significant allocation of manpower, leading to considerable expenses. This workforce is drawn from various sectors like banking, postal services, and education. Their extensive participation in activities such as pre-voting training, travel, and overseeing the entire voting process disrupts the routine operations of their respective sectors for a considerable duration. Additionally, there are concerns such as tampering of Electronic Voting Machines (EVMs) and the improper use of ballot papers, raising doubts about the legitimacy of the voting procedure. Moreover, individuals who are not residing in their hometowns face difficulties in voting remotely. A potential remedy to address all these issues is to implement an online voting system. In online system it is important to authenticate every user to ensure that genuine voter is casting his/her vote. This  work proposes a three-layer security-based e-voting system. Firstly, voter’s authenticity is validated against both Voter ID and Aadhar ID followed by OTP checking. In the next level verification is done based on face detection and recognition using Haar Cascade Clas-sifier Algorithm and Local Binary Pattern Histogram Algorithm. Each voter can access to the system only when being recognized with Registered Voter Data-base. Once the corresponding face is matched with the information provided, the voter is allowed to proceed for choosing preferred candidate from the panel. The contribution of this  work is the proposal of an authentic voting system but at a fraction of cost requiring minimal manpower.

## Objective

This research work aims to replace the existing voting system to a digitally managed online voting system to save time and cost as well as to ensure the authenticity of the voting process. The system can perform tasks like voter registration, vote polling and result announcement.
The user/voter will be able to login to the system with their Voter Id and Aadhar ID and cast a vote. This system will also have the provision to calculate and print the results after the election. Specifically, the system will be designed to ensure:

**• Privacy:** No one will be able to know to whom a voter casted his/her vote.

**• Authenticity:** Only enlisted authentic voter can cast his/her vote.

**• Integrity:** No alternation of vote is permitted.

**• No location dependency:** Eligible voter can caste his/her vote from any location across the world provided he/she is authenticated by the system through the three-step process.
Moreover, for faster face recognition the training images are stored following a nu-meric nomenclature that reduces the search space drastically.

##  Proposed Methodology
This research work presents a three-level security based electronic voting system. These levels are described below:

**• Level 1: Unique Voter ID and Aadhaar ID verification:** At the time of voter reg-istration, system will request for the unique Voter ID and Aadhaar ID from the voter. The entered unique ids are verified from the government records and stored in local Registered Voter Database (RVD). At the time of vote polling, voters need to enter the unique IDs once again which are verified against the local RVD.

**• Level 2: OTP verification:** During the voter registration process, user needs to enter a mobile number for OTP verification purpose which gets stored in the local RVD. At the time of vote polling, OTP is sent to the registered mobile number which if correctly matches then the voter can enter to the face recognition panel.

**• Level 3: Face recognition:**  During voter registration, the system captures user im-age through webcam. This captured image is converted into 100 gray scale images where each image is named as VoterID_number.i where i=1 to 100. All these images are stored in a XML file for all registered voters. This file containing the face data is used for training the algorithm used for face detection and recognition. At the time of vote polling, when the voter is directed to the face recognition panel, webcam captures real-time image and then using Haar Casacade Classifier Algorithm face is detected. This process is carried out very fast at real-time as it needs to check with only 100 images against each voter and those images are stored using numeric no-menclature based on voter id number. After this, applying Local Binary Pattern Histogram (LBPH) Algorithm on the detected face, if a voter is correctly recognized by matching with the trained face dataset, a green rectangle appears and the voter is allowed to successfully log into the system. Otherwise, if face detection and recog-nition fail, a red rectangle around the face appears and the voter is denied to access the system.

The entire work is shown from two perspectives: voter registration whose process diagram is shown in Fig.1 and vote polling whose process diagram is depicted in Fig. 2.

<img src ="https://github.com/geekymonk123/E-voting-system/blob/main/voter%20reg.jpg" alt="MLBC">

**Fig. 1. Process Diagram of Voter Registration**

<img src="https://github.com/geekymonk123/E-voting-system/blob/main/vote_poling.jpg" alt="MLBC">

**Fig. 2. Process Diagram of Vote Polling**

## Haar Cascade Classifier Algorithm

It is an object detection algorithm used to iden-tify faces in an image or real time video and uses edge or line detection features. The algorithm is provided with many positive images that consists of faces, and many neg-ative images that do not consist of faces to train. In the repository the models are stored in XML files. The first contribution to the research was the introduction of the haar features on the image, which make it easier to find out the edges or lines in the image, or select areas where the pixel intensities suddenly change. The darker areas in the haar feature are pixels with a value 1, and the lighter areas are pixels with a value 0. Each of these is responsible for finding out a specific feature in the image, for example an edge, a line or any structure in the image where there is a sudden change of intensities. The goal here is to determine the sum of all image pixels that are in darker area of the haar feature and the sum of all the image pixels that are in the lighter area of the haar feature and then to find out their difference. A flow diagram of Haar Cascade Classifier Algo-rithm for face detection is shown in Fig. 3.

<img src="https://github.com/geekymonk123/E-voting-system/blob/main/Haar%20Cascade%20Classifier.jpg" alt="MLBC">

## Local Binary Pattern Histogram Algorithm

Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighbourhood of each pixel and considers the result as a binary number. Using the LBP combined with histograms we can represent the face images with a simple data vector. As LBP is a visual descriptor it can also be used for face recognition tasks.

<img src="https://github.com/geekymonk123/E-voting-system/blob/main/LBP.jpg" alt="MLBC">




