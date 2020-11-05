from hub import Dataset, features

# Create dataset
ds = Dataset(
    "./data/example/pytorch",
    shape=(64,),
    schema={
        "image": features.Tensor((512, 512), dtype="float"),
        "label": features.Tensor((512, 512), dtype="float"),
    },
)

# tansform into Tensorflow dataset
ds = ds.to_tensorflow().batch(8)

# Iterate over the data
for batch in ds:
    print(batch["data"], batch["labels"])
