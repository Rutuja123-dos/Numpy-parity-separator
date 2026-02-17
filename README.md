## NumPy Even-Odd Separator 🔢
A high-performance Python tool designed to separate numerical data into distinct Even and Odd categories using NumPy Vectorization.

🚀 The Challenge
Most beginners use for loops and .append() to sort numbers. While that works, it is slow for large datasets. This project demonstrates how to use Normal Logic combined with NumPy's power to process data all at once.

🛠️ Features
* User Input Integration: Accepts a list of numbers directly from the terminal.

* Vectorized Processing: Uses Boolean masking for instant data separation.

* Memory Efficient: Leverages NumPy arrays for better performance compared to standard Python lists.

* 🧠 Technical Logic: Boolean Masking
Instead of checking numbers one by one, this project uses the following logic:

# Even mask
even = numbers[numbers % 2 == 0]

# Odd mask
odd = numbers[numbers % 2 != 0]
This allows the computer to check every number in the array simultaneously, which is a key requirement for data engineering roles at companies like Adobe or Pinterest.
## Technologies Used
1. Python
2. Numpy

## 📂 How to Run
1. Clone this repository:
git clone https://github.com/your-username/numpy-parity-separator.git

2.Install dependencies:
pip install numpy

3.Run the script:
python main.py

## Author
Rutuja Wagh
