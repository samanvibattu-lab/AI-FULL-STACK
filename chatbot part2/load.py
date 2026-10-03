from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("segmind/tiny-sd")

print("Model loaded successfully!")