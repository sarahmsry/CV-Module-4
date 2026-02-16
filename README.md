# CV-Module-4: Thermal Image Animal Boundary Detection

Script to find the exact boundaries of animals in thermal imaging camera images using openCV.

## Overview

Detects and segments animal boundaries in thermal images using image processing techniques optimized for thermal data. The approach combines binary thresholding and contour analysis to isolate animals from the background.

## Features

- **Automatic thermal segmentation** - Uses Otsu's thresholding for adaptive threshold determination
- **Noise filtering** - Gaussian blur
- **Multi-animal detection** - Handles images with multiple animals
- **Boundary refinement** - Edge detection refines final contour

## How It Works

### Algorithm Pipeline

1. **Grayscale Conversion** - Convert BGR thermal image to grayscale
2. **Histogram Equalization** - Improve contrast in thermal regions
3. **Blur** - Gaussian blur (9×9) to reduce noise
4. **Binary Thresholding** - Otsu's method automatically separates hot animals from cold background
5. **Contour Detection** - Find all connected components
6. **Filtering** - Keep contours between min_area (2000px) and max_area (150000px)

## Requirements

- Python 3.7+
- OpenCV (cv2)
- NumPy

## Installation

```bash
pip install opencv-python numpy
```

## Usage

### Basic Usage - Process Single Image

```python
from find_boundary import find_boundary

image_path = r"your image path"
find_boundary(image_path)
```

### Batch Processing - All Images in Folder

```bash
python find_boundary.py
```

The script automatically processes all `.jpg`, `.jpeg`, and `.png` files in the test folder and displays:
- Binary mask showing detected animals
- Original image with green contours and blue bounding boxes

Press any key to advance/close window

## Parameters

Edit these values in `find_boundary()` to tune for your images:

```python
blur_kernel = (9, 9)           # Gaussian blur kernel size
min_area = 2000                # Minimum contour area (pixels)
max_area = 150000              # Maximum contour area (pixels)
```

### Adjusting for Different Conditions

**Too much background detected:**
- Increase `min_area` to filter smaller false positives
- Decrease `closing_iterations`

**Animals fragmented (not fully connected):**
- Increase `closing_kernel` size
- Increase `closing_iterations`

**Too much noise remaining:**
- Increase `erosion_iterations`
- Increase blur kernel size

## Output

For each processed image, the script displays and logs:
- **Total contours found** - Raw number before filtering
- **Significant contours** - Number of contours meeting size criteria
- **Visual windows:**
  - Binary Mask - Thresholded thermal regions
  - Animal Boundaries - Original image with detected boundaries

## Comparison to SAM2 (Segment Anything Model 2)

| Aspect | This Script | SAM2 |
|--------|------------|------|
| **Approach** | Classical CV (thresholding + morphology) | Deep learning segmentation |
| **Speed** | Very fast (<100ms/image) | Slower (requires GPU for real-time) |
| **Accuracy** | Good for uniform thermal signatures | Excellent for complex scenes |
| **Dependencies** | Minimal (OpenCV + NumPy) | Heavy (PyTorch, vision models) |
| **Flexibility** | Limited to thermal properties | Works on any image type |
| **Training Required** | No | Yes (or use pretrained) |
| **Offline Capability** | Full | Full |

**Best for:** Thermal-specific applications with consistent imaging conditions

## Troubleshooting

**"No contours found"**
- Check image is actual thermal image
- Increase blur or lower Canny thresholds
- Lower `min_area` threshold

**"Only eyes/legs detected, not whole animal"**
- Increase `closing_iterations` (connect fragments)
- Increase `closing_kernel` size
- Lower Canny thresholds

**"Too much background in detection"**
- Increase `min_area` threshold
- Increase `max_area` or decrease to filter huge regions
- Increase `erosion_iterations`
