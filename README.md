> [!CAUTION]
> Though I have done everything in my best effort to ensure there is zero chance of corruption to your files,
> I cannot guarantee or be held liable for any loss of data that may arise from using this tool, and any
> responsibility lies on you, the user, to use this tool appropriately and understand the risks.

# KwikSort
**Kwiksort** is a basic file sorter created to sort your images into the relevant directories based off their _EXIF_ data.

## How it works
It creates directories using the EXIF data, then moves them based on YEAR and MONTH as YYYY, MM

![image](https://github.com/user-attachments/assets/1bd4c058-93cf-4274-8513-a611bafb08bf)


## Get started
1) Place the ```kwiksort.py``` file in the desired folder _(This folder must contain all your images)_
2) Run the file
3) Read the disclaimer and run the tool
   
```
!!! IMPORTANT !!!

KWIKSORT is to be used at your own risk.
Though I have done everything in my best effort to ensure there is zero chance of corruption to your files,
I cannot guarantee or be held liable for any loss of data that may arise from using this tool, and any
responsibility lies on you, the user,to use this tool appropriately and understand the risks.
Having said that, I hope you enjoy this neat little tool :-)

(RETURN) RUN KWIKSORT NOW | (E) EXIT
>>>
```

4) Depending on the amount/size of images/files, the sorter should take roughly 30 seconds for 3000+
```
4 files touched! Exiting program ...
```
5) It has now sorted the files into the following directory structure:
```
|----2021-----|
|-------09----|
|----2024-----|
|-------03----|
|-------04----|
```
![image](https://github.com/user-attachments/assets/cba7f5c4-4b35-44ac-bec4-7ee44a1a208f)

> [!NOTE]
> Kwiksort will handle video files differently. All video files will be placed into the 'None' folder.
> This is currently something I am working on as it currently only handles images with EXIF data based on year and month captured.
> That being said, any files without this data will also be stored in the 'None' folder.
