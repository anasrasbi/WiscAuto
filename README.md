# WA -  Coding Challenge

My attempt to solve a basic coding challenge of object detection using openCV, for my application to the Wisconisn Autonomous (WA) student org.


## Methodolgy

The method I used was detecting the cones based on their color (red) and finding the center of each cone. When doing so, I only focused on my ROI - region of interest, to avoid detecting unnecessary objects like the exit signs or the furniture. Then I drew two converging lines where each line represents the slope of either the left or right lane of cones.

## Result
![Answer](https://raw.githubusercontent.com/anasrasbi/WiscAuto/main/answer.png)

## Other Approaches
In my first attempt, I tried using Canny + Hough Transform to detect lines, but it captured unnecessary lines (e.g., floor tiles) and it didn't even notice the cones. This approach didn't work because it was looking for lines, which can work fine for road lanes but not objects like cones.

## Libraries
cv2 (openCV), matplotlib, and numpy.
