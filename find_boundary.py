import cv2
import os

def find_boundary(image_path):
    image = cv2.imread(image_path)
  
    # Convert image to grayscale 
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

    # Apply histogram equalization to increase contrast 
    gray_image = cv2.equalizeHist(gray_image)
    
    # Apply Gaussian blur to reduce noise
    blur_image = cv2.GaussianBlur(gray_image, (9, 9), 0)

    # Use binary thresholding with Otsu's method to create a binary mask
    _, binary = cv2.threshold(blur_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours by area to remove noise 
    min_area = 2000  # Only keep larger contours 
    max_area = 150000  # Filter out if too large 
    filtered_contours = []
    for c in contours:
        if min_area < cv2.contourArea(c) < max_area:
            filtered_contours.append(c)
    
    print(f"Image: {os.path.basename(image_path)}")
    print(f"Total contours found: {len(contours)}, Significant contours: {len(filtered_contours)}")

    # Draw filtered contours and bounding boxes on the image
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, filtered_contours, -1, (0, 255, 0), 2)
    
    # Draw bounding boxes around each animal
    for contour in filtered_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image_with_contours, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Binary Mask', binary)
    cv2.imshow('Animal Boundaries', image_with_contours)
    cv2.waitKey(0) # Press any key to close

if __name__ == "__main__":
    test = 'test.jpg'  
    find_boundary(test)
    cv2.destroyAllWindows()
    