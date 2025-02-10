# WA - Perception Coding Challenge

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Function to mask region of interest
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

# Function to draw converging lines
def draw_converging_lines(img, left_points, right_points):
    img = np.copy(img)
    blank_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    height, width = img.shape[:2]

    def fit_and_draw_line(points, color):
        if len(points) > 1:
            points = np.array(points)
            x = points[:, 0]
            y = points[:, 1]

            # Fit a linear model (y = mx + b)
            m, b = np.polyfit(x, y, 1)

            # Define start and end points
            y1 = height  # Bottom of image
            x1 = int((y1 - b) / m)  # Solve for x at y1

            y2 = int(height * 0)  # Upper part of image
            x2 = int((y2 - b) / m)  # Solve for x at y2

            # Draw the line
            cv2.line(blank_img, (x1, y1), (x2, y2), color, thickness=5)

    # Fit and draw left lane
    fit_and_draw_line(left_points, (0, 255, 0))  # Green

    # Fit and draw right lane
    fit_and_draw_line(right_points, (0, 255, 0))  # Green

    # Merge with original image
    img = cv2.addWeighted(img, 0.8, blank_img, 1, 0.0)
    return img

# Load and preprocess image
image = cv2.imread('red.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width = image.shape[:2]

# Convert to HSV for color filtering
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# Define red color range in HSV
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# Create masks to detect red cones
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

# Apply region of interest mask
roi_vertices = [
    (width * -0.1, height),
    (width * 0.4, height * 0.25),
    (width * 0.7, height * 0.25),
    (width + width * 0.15, height)
]
masked_image = region_of_interest(mask, np.array([roi_vertices], np.int32))

# Find contours of cones
contours, _ = cv2.findContours(masked_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Extract center points of cones
left_points = []
right_points = []
for contour in contours:
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])  # X coordinate
        cy = int(M["m01"] / M["m00"])  # Y coordinate

        # Classify into left or right based on image center
        if cx < width // 2:
            left_points.append((cx, cy))
        else:
            right_points.append((cx, cy))

# Sort left and right points from bottom to top
left_points = sorted(left_points, key=lambda p: p[1], reverse=True)
right_points = sorted(right_points, key=lambda p: p[1], reverse=True)

# Draw detected cones
for point in left_points + right_points:
    cv2.circle(image, point, 10, (0, 255, 0), -1)  # Green dots on cones

# Draw converging lines
drawn_img = draw_converging_lines(image, left_points, right_points)

# Save the output as "answer.png"
cv2.imwrite("answer.png", cv2.cvtColor(drawn_img, cv2.COLOR_RGB2BGR))

# Display the result
plt.imshow(drawn_img)
plt.axis("off")
plt.show()

