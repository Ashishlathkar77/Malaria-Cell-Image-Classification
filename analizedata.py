import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def generate_dataset(path):
    data = {'imgpath': [], 'labels': []}

    folders = os.listdir(path)

    for folder in folders:
        folderpath = os.path.join(path, folder)
        files = os.listdir(folderpath)

        for file in files:
            filepath = os.path.join(folderpath, file)

            data['imgpath'].append(filepath)
            data['labels'].append(folder)

    return pd.DataFrame(data)

path = '/kaggle/input/cell-images-for-detecting-malaria/cell_images'

dataset = generate_dataset(path)

# Drop the 'cell_images' label if it exists
value_to_drop = 'cell_images'
dataset = dataset[dataset['labels'] != value_to_drop]

# Plot a grid of sample images
def plot_image_grid(dataset, num_rows, num_cols):
    plt.figure(figsize=(20, 25))

    shuffled_dataset = dataset.sample(frac=1).reset_index(drop=True)

    num_samples = min(len(shuffled_dataset), num_rows * num_cols)

    for i in range(num_samples):
        plt.subplot(num_rows, num_cols, i + 1)
        row = shuffled_dataset.iloc[i]
        image_path = row['imgpath']
        image = Image.open(image_path)
        plt.imshow(image)
        plt.title(row["labels"], fontsize=18, fontweight='bold')
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# Display a grid of sample images
plot_image_grid(dataset, 3, 3)
