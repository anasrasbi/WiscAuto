answer.png
This image shows the detected path boundaries drawn using straight converging lines.

Methodology
Load Image: Read and convert the image to RGB format.
Preprocessing: Convert the image to grayscale and apply Canny edge detection to highlight edges.
Region of Interest (ROI): Mask everything except the relevant area to focus on the path.
Hough Transform: Detect lines using cv2.HoughLinesP().
Lane Detection:
Extract left and right boundary points from detected lines.
Fit a straight line to each side using linear regression (np.polyfit).
Extend the lines from the bottom to the top of the image for a clear boundary.
Draw and Save: Draw the detected boundary lines on the image and save the output as "answer.png".
What Did I Try and Why It Did Not Work?
Initial Attempt: Detected all edges using Canny + Hough Transform, but it captured unnecessary lines (e.g., floor tiles).
Issue: The detection was noisy, resulting in zigzag lines instead of smooth lane boundaries.
Solution: Instead of using raw detected lines, I calculated an average slope for left and right lanes, then extended them as two clean boundary lines.
Libraries Used
opencv-python (cv2) → Image processing, edge detection, Hough transform.
numpy → Handling arrays and performing linear regression.
matplotlib → Displaying the image.
