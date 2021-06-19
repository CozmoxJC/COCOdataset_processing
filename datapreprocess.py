import fiftyone as fo

dataset = fo.Dataset(
    name="filtered_dataset",
    persistent="C:\\Users\\user\\Desktop\\Dataset\\filtered",
    overwrite=fo.types.COCODetectionDataset,
)

# Load your FiftyOne dataset
dataset = fo.load_dataset(dataset)

# Launch the app
session = fo.launch_app(dataset, port=5151)
