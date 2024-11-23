import os  # Import the 'os' module for creating directories and handling file paths.
import cv2  # Import OpenCV library for handling video capture and image processing.
import time  # Import 'time' module for adding delays (useful for timing image collection).
import uuid  # Import 'uuid' module to generate unique identifiers for image filenames.

# Define the path where images will be saved.
IMAGE_PATH = "CollectedImages"

# Define the labels for which images will be collected.
labels = ["Hello", "Yes", "No", "Thanks", "IloveYou", "Please"]

# Define the number of images to capture per label.
number_of_images = 5

# Loop through each label in the `labels` list.
for label in labels:
    # Create a folder for the current label inside the IMAGE_PATH directory.
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(
        img_path, exist_ok=True
    )  # Create directory if it doesn't already exist.

    # Open the camera for capturing images.
    cap = cv2.VideoCapture(0)  # Use camera index 0 (default camera).
    print(
        f"Collecting images for {label}"
    )  # Notify the user which label is being processed.
    time.sleep(3)  # Wait for 3 seconds before starting image collection.

    # Loop to capture the specified number of images.
    for imgnum in range(number_of_images):
        # Capture a frame from the camera.
        ret, frame = (
            cap.read()
        )  # `ret` is a boolean indicating success, `frame` is the image captured.

        # Define a unique filename for the image using the label and UUID.
        imagename = os.path.join(
            IMAGE_PATH, label, label + "." + "{}.jpg".format(str(uuid.uuid1()))
        )

        # Save the captured frame as an image file.
        cv2.imwrite(imagename, frame)  # Save the frame to the specified path.

        # Display the captured frame in a window.
        cv2.imshow("frame", frame)  # Open a window named 'frame' to show the image.

        time.sleep(2)  # Wait for 2 seconds before capturing the next image.

        # Break the loop if the 'q' key is pressed.
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break  # Exit the loop early if the user presses 'q'.

    # Release the camera once image collection for this label is complete.
    cap.release()  # Frees up the camera resources.
