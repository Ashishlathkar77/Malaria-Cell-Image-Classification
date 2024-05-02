# Malaria Cell Image Classification

---

## Introduction:

Welcome to the Malaria Cell Image Classification project, a groundbreaking endeavor aimed at leveraging cutting-edge technology to combat malaria, a life-threatening disease that affects millions of people worldwide. In this project, we focus on utilizing machine learning techniques to develop an automated system capable of accurately classifying microscopic images of blood cells as either infected or uninfected with the malaria parasite.

The dataset used in this project is sourced from the official NIH website and comprises two main categories: "Infected" and "Uninfected". With a total of 27,558 images, this dataset provides a rich and diverse collection of malaria-infected and healthy blood cell images, enabling us to train and evaluate our machine learning models effectively.

Our primary objective is to develop a robust classification model that can accurately distinguish between malaria-infected and uninfected blood cells. By achieving this goal, we aim to streamline the process of malaria diagnosis, particularly in resource-constrained settings where access to skilled healthcare professionals may be limited.

Through this project, we seek to harness the power of technology to make a meaningful impact in the fight against malaria. By automating the diagnosis process, we can expedite treatment and improve health outcomes for individuals affected by this devastating disease.

## Samples Visualization: 

The process of generating a dataset from a directory containing images of malaria-infected and uninfected cells. It then plots and saves four pairs of infected and uninfected cell images for visualization purposes.

Here's a breakdown of how this task was approached:

1. **Data Directory Setup**: The first step is to define the path to the data directory containing the images. In this case, the directory is '/kaggle/input/cell-images-for-detecting-malaria/cell_images'.

2. **Dataset Generation Function**: A function named `generate_dataset` is defined to traverse through the data directory and create a DataFrame containing the image paths and corresponding labels (infected or uninfected). This function iterates over the subdirectories within the main data directory, reads each image file, and appends its path and label to the DataFrame.

3. **DataFrame Creation**: The `generate_dataset` function is called to create a DataFrame named `dataset`, which contains the image paths and labels.

4. **Plotting and Saving Samples Function**: Another function named `plot_and_save_samples` is defined to visualize and save sample pairs of infected and uninfected cell images. This function randomly samples one infected and one uninfected image from the dataset DataFrame, reads and plots them using Matplotlib, and then saves the plot as a PNG file. This process is repeated for the specified number of pairs.

5. **Visualization and Saving**: Finally, the `plot_and_save_samples` function is called to generate four pairs of infected and uninfected cell images and save them in a directory named 'sample_images'.

This approach allows for the efficient generation of a dataset DataFrame and the visualization of sample images, enabling quick inspection of the data and verification of its integrity before proceeding with further analysis or model training.

First Sample:

![first_image](https://github.com/Ashishlathkar77/Malaria-Cell-Image-Classification/blob/main/Visualizations/sample_1.png)

Second Sample:

![first_image](https://github.com/Ashishlathkar77/Malaria-Cell-Image-Classification/blob/main/Visualizations/sample_2.png)

Third Sample:

![first_image](https://github.com/Ashishlathkar77/Malaria-Cell-Image-Classification/blob/main/Visualizations/sample_3.png)

Fourth Sample:

![first_image](https://github.com/Ashishlathkar77/Malaria-Cell-Image-Classification/blob/main/Visualizations/sample_4.png)

## MalariaDataset and Transformations:

Defines a custom dataset class called `MalariaDataset` for handling malaria cell images. Additionally, it includes preprocessing and transformation steps using PyTorch's `transforms` module.

Here's how this approach was implemented and can be described for a report:

1. **Custom Dataset Class (MalariaDataset)**:
   - The `MalariaDataset` class is created by subclassing `torch.utils.data.Dataset`, making it compatible with PyTorch's data loading utilities.
   - It initializes with parameters such as the directory containing the image data (`image_dir`) and any desired transformations (`transform`).
   - In the constructor (`__init__` method), it populates lists of image paths (`self.images`) and corresponding labels (`self.labels`). Labels are assigned based on the subdirectory names within the `image_dir`.
   - The `__len__` method returns the total number of images in the dataset.
   - The `__getitem__` method retrieves an image and its corresponding label at a given index. It reads the image using OpenCV, converts it to RGB format, and applies any specified transformations.
   - Exception handling is implemented to handle cases where images cannot be read. In such cases, a placeholder image is returned with a dummy label.

2. **Preprocessing and Transformation**:
   - Transformation operations are defined using PyTorch's `transforms.Compose` class, allowing for sequential application of transformations.
   - Two transformations are specified: resizing images to a fixed size of 120x120 pixels and converting images to tensors using `transforms.ToTensor()`.
   - These transformations are then applied to the images in the dataset during training or inference.

3. **Data Loading and Visualization**:
   - The dataset is instantiated (`dataset = MalariaDataset(image_dir=image_dir, transform=test_transforms)`), providing the directory containing the malaria cell images and the defined transformations.
   - The length of the dataset is printed to verify the number of images.
   - Five sample pairs of images are selected from different classes (infected and uninfected) for visualization. These images are converted to NumPy arrays and plotted using Matplotlib.
   - Class counts are calculated to determine the distribution of images across different classes in the dataset.

This approach provides a structured and scalable solution for handling image data, including loading, preprocessing, and transformation, making it suitable for training deep learning models for malaria cell image classification.
