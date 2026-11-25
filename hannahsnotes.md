11/24/26

#Submitted pull request:
requirements.txt needs to list torchvision because ultralytics requires it. 

#Other issues
in test.py, in this line:
```metrics = model.val(data='data/data.yaml', imgsz=1600, batch=1,
                    conf=0.25, iou=0.6, device=device, split='test', max_det=600)```
device needed to be set to `device` and not 0 in order to keep the settings above it. 

A similar thing needed to be done in inference_on_raw_imgs.py:
detection_model = AutoDetectionModel.from_pretrained(
        model_type='ultralytics',
        model=model,
        confidence_threshold=confidence,
        device="cpu",
    ) 
except 'device' wasn't defined above. 

in inference_on_raw_imgs.py, there is no file called './best.pt'. There is a file called 'best_weights.pt', but that doesn't work (generates error "ValueError: Category names not available. Please provide category_mapping for ONNX models). Apparently the mappings/structure is missing, and best_weights.pt is just the weights for the network. 
 

Next up:
- make box edges smaller so can actually tell what's inside?
- try on later-season images?