def setup():
  import subprocess
  def pip_install(name):
    subprocess.call(['pip', 'install', name])
  pip_install('azure-storage-blob')
  pip_install('ultralytics')  

def download_model():
  from azure.storage.blob import BlobServiceClient
  
  # Define your Azure Storage account credentials
  connection_string = "DefaultEndpointsProtocol=https;AccountName=geodata059;AccountKey=gVk2/U/8lqbFfIGSrDBlwzPQMJOyzLNil6ySE2p5E8Mol+TeUHl5h9hJDe5In1fgDNGMcHpW+91c+AStLGPMqg==;EndpointSuffix=core.windows.net"
  container_name = "core"
  blob_name = "best (5).pt"
  
  # Create a BlobServiceClient using the connection string
  blob_service_client = BlobServiceClient.from_connection_string(connection_string)
  
  # Get a reference to the container
  container_client = blob_service_client.get_container_client(container_name)
  
  # Get a reference to the blob
  blob_client = container_client.get_blob_client(blob_name)
  
  # Download the blob data to a local file
  with open("best (5).pt", "wb") as f:
      data = blob_client.download_blob()
      data.readinto(f)

def predict_facies(path_to_core_image, path_to_model):
  import matplotlib.pyplot as plt  
  import ultralytics
  ultralytics.checks()
  from ultralytics import YOLO
  
  model1 = YOLO(path_to_model)
  result = model1.predict(source=path_to_core_image, 
                 imgsz=640, iou=.3, save=True, 
                 save_txt=True, save_conf=True, show_labels=False)  
  
  # Visualize result
  for i in range(len(result)):
      plt.figure(figsize=(5,5))
      plt.imshow(result[i].plot())
      plt.show()  
