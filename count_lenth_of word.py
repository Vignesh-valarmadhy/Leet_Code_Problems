# Define the given text
text = """
Brain tumor segmentation is a critical and challenging task in medical image analysis, essential for improving patient outcomes through timely detection and treatment. Manual segmentation is laborious and subjective, necessitating efficient automated solutions. Deep learning, particularly U-Net models, has shown significant potential in biomedical image segmentation. The diversity in tumor location, shape, and size complicates automatic segmentation, requiring differentiation of abnormal from normal tissues (WM, GM, CSF) in modalities like MRI. Multimodal approaches (e.g., PET/CT, PET/MRI) enhance accuracy by integrating data from various sources. Our proposed model, trained on the BRATS 2019 dataset, demonstrated superior performance with Dice Scores of 0.913, 0.872, and 0.805, outperforming traditional models like VGG and FCN. This method, notable for its performance, success, and preprocessing structure, is highly adaptable for various applications."""



# Count the number of characters in the text
num_characters = len(text)
print("Number of characters in the text:", num_characters)
