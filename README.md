# Inroductory Data Science Task 1: Creating Cmbination Thumbnails

## Use Cases of the Project
This project, as an introductory data science task, leverages digital image processing techniques to load, process, and combine product images from various fashion categories (dresses, shoes, accessories) to generate virtual outfit combinations with transparent backgrounds.

### Real-World Application
The code and generated thumbnails from this project have been successfully utilized in the combination image workflows of **FeshFed**, a major company with 100 million monthly users.


## Thumbnail Results : 


<div align="center">
  <table>
    <tr>
      <td><img src="https://github.com/aysenurkocaak/photo/blob/main/WhatsApp%20Image%202024-09-01%20at%2004.31.36%20(3).jpeg" width="300"></td>
      <td><img src="https://github.com/aysenurkocaak/photo/blob/main/WhatsApp%20Image%202024-09-01%20at%2004.31.36%20(2).jpeg" width="300"></td>
      <td><img src="https://github.com/aysenurkocaak/photo/blob/main/WhatsApp%20Image%202024-09-01%20at%2004.31.36.jpeg" width="300"></td>
    </tr>
    <tr>
      <td><img src="https://github.com/aysenurkocaak/photo/blob/main/WhatsApp%20Image%202024-09-01%20at%2004.31.36%20(6).jpeg" width="300"></td>
      <td><img src="https://github.com/aysenurkocaak/photo/blob/main/WhatsApp%20Image%202024-09-01%20at%2004.31.36%20(5).jpeg" width="300"></td>
      <td><img src="https://github.com/aysenurkocaak/photo/blob/main/WhatsApp%20Image%202024-09-01%20at%2004.31.36%20(1).jpeg" width="300"></td>
    </tr>
  </table>
</div>



### Solution Overview
To address this task, we developed a Python function that:
1. **Processes Images**:
   - Loads images with their category metadata.
   - Handles transparency (RGBA channels) to ensure seamless blending onto a white background.

2. **Dynamic Layout**:
   - Identifies whether a dress is included in the items and adjusts the layout accordingly:
     - **With Dress**: Focuses on a vertical layout to emphasize the dress.
     - **Without Dress**: Uses a balanced grid layout for items like tops, bottoms, and accessories.
   - Adapts to both 3-item and 4-item scenarios.

3. **Scaling and Placement**:
   - Resizes images proportionally to fit the thumbnail canvas without distortion.
   - Dynamically calculates positions for each item to avoid overlap and maintain a visually appealing composition.

4. **Output**:
   - Generates and saves the thumbnail as a PNG file for further use.

### Code Highlights
- **Dynamic Image Layout**: The function uses logic to determine layouts based on the presence of a dress and the number of items.
- **Transparency Handling**: Ensures smooth integration of transparent images into the canvas.
- **Scalability**: Designed to handle additional clothing categories or layout rules with minimal modifications.

