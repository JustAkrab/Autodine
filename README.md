# Food Delivery Web App Frontend

## Project Overview
This is the frontend part of a food delivery web application. It displays a variety of food items, each having its own card with details like title, rating, and ingredients. The frontend interacts with a server to fetch orders and highlights the relevant food items and their modifications. It also includes a smooth scrolling feature across the page to enhance user experience.

## Folder Structure
```
/front
  ├── index.html
  ├── front/styles.css
  ├── images/
  ├── script.js
```

### 1. index.html
This is the main entry point for the application, containing the structure of the food items, along with their images, titles, and ratings. The ingredients for each food item are hidden by default and are highlighted when an order is fetched from the server.

#### Key Components:
- **HTML structure**: Each food item is represented by a card element (`div` with class `card`).
- **Ratings**: A star rating system using simple `<span>` elements.
- **Ingredients**: Ingredients for each item are hidden within the `.ingredients` div but can be revealed dynamically through JavaScript when an order is fetched.
- **JavaScript Integration**: The page includes the `script.js` file to enable dynamic behavior like smooth scrolling and highlighting orders.

### 2. script.js
This JavaScript file handles the dynamic functionalities of the web app, including:
- **Smooth Scrolling**: Automatically scrolls down the page and scrolls back up in a loop, providing an automated page view feature.
- **Highlighting Orders**: Fetches the user's order data from a server (simulated locally in the code) and highlights the corresponding food items. Modifications (e.g., extra cheese or no onions) are visually highlighted in blue.

#### Key Functions:
- `smoothScroll()`: Implements smooth, continuous scrolling of the page up and down, creating an animated browsing experience.
- `highlightCards()`: Fetches the order data (currently mocked), identifies the corresponding food items on the page, and highlights the ordered food and modifications with a visual scaling and color highlight effect.

### 3. front/styles.css
Contains all styles for the web app, including layout, font sizes, colors, hover effects, and transition animations. It is linked within `index.html`.

### 4. images/
This folder contains all the food item images (e.g., `eggsan.jpg`, `burger.jpg`) used to visually represent the items on the page. Each image is linked directly within the corresponding card in `index.html`.

## How It Works
1. When the page loads, the `highlightCards()` function is called.
2. This function mocks a fetch request to retrieve the user's order and looks for matching food items on the page.
3. Once it finds the food items, it highlights the card and any relevant modifications (such as adding cheese or removing tomato) by changing their background color and applying a zoom effect on the card.
4. The `smoothScroll()` function automatically scrolls down and up across the page in a loop, pausing briefly before changing direction.

## How to Run
To run this frontend:
1. Clone the repository or download the source files.
2. Open the `index.html` file in your web browser.
3. The page will automatically load and start scrolling. Highlighted items will simulate an order being fetched.

### Future Enhancements:
- **API Integration**: Replace the mocked data in `highlightCards()` with real data from a backend API.
- **Order Management**: Add functionality for users to place orders and customize their food preferences.
- **Mobile Responsiveness**: Improve the layout to adapt to different screen sizes.
  
