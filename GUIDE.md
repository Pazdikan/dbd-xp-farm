
# DBD XP Farm Installation Guide

Welcome to the DBD-XP-Farm installation guide! Follow these steps carefully to set up the application and avoid common pitfalls. ✨

---

## Prerequisites

Before proceeding, ensure the following:

1. **Python Version**: Make sure you are using python version 3.12.* The script will not work on any other version. After installing 3.12 please make sure, it's added to system enviroment variables. Restart your terminal or Windows, and run the python --version command again.

```bash
python --version
```

2. **Graphics Card Requirements**: Make sure your GPU supports CUDA. [Click here to download CUDA](https://developer.nvidia.com/cuda-downloads).

   - This is the only thing you have to install by yourself.

3. **System Requirements**: Ensure your PC can run Dead by Daylight smoothly without the script. This is important because the script uses screen reading (takes lots of screenshots) to determine what's happening in game.

   - Note: The screenshots do not take up your storage, they exist temporarly in RAM.

---

## Installation Steps

### Option 1: Download ZIP File (Recommended)

> [!NOTE]  
> Why is this recommended instead of git? Well the versioned releases are ~~always~~ *usually* working. Sometimes I may push some unfinished or untested code into the main branch, making the script broken.

> [!IMPORTANT]
> You will have to download new versions manually.

1. **Download the Repository as a ZIP File**:
   - Go to the GitHub repository and click on the **Code** button.
   - Select **Download ZIP**.

2. **Extract the ZIP File**:
   - Extract the contents of the ZIP file to a folder of your choice.

3. **Run the Setup Script**:
   - Navigate to the extracted folder.
   - Run `setup.bat` to install the required dependencies.

4. **Reinstall NVIDIA Driver**:
   After running the setup script, **reinstall your NVIDIA driver** and reboot your PC.

### Option 2: Using Git

> [!TIP]
> When installed via git, you can run git pull command to automatically update your script.

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-repo/dbd-xp-farm.git
   cd dbd-xp-farm
   ```

2. **Install Requirements**:
   Run the following command to install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Reinstall NVIDIA Driver**:
   After installing the requirements, **reinstall your NVIDIA driver** and reboot your PC.

   - This step is crucial to avoid any compatibility issues. 🚜⚙️


---

## In-Game and Windows Settings

1. Make sure you are using a 1920x1080p resoluton, if you are on a higher resolution display, you can change it in Windows display settings.

2. Make sure you are using 100% resolution scale, no upscalling and 100% GUI scale for both menu and in-game.

---

## Launch Options (Optional)

If you encounter issues with software like ReShade, do the following:

- Add `-dx12` to your Steam or Epic launch options.
- Reinstall your NVIDIA driver again and reboot your PC.

  This ensures your CPU doesn’t run into problems where it unnecessarily re-caches shaders and objects, which can cause performance drops. 🚑

### How to Add Launch Options:

- **Steam**:
  1. Right-click Dead by Daylight in your library.
  2. Go to **Properties** > **General**.
  3. Under **Launch Options**, add `-dx12`.
- **Epic Games Launcher**:
  1. Go to **Settings**.
  2. Scroll down to **Dead by Daylight** under **Manage Games**.
  3. Check **Additional Command Line Arguments** and add `-dx12`.

---

## Notes on Performance

🔧 This script lightly relies on your system’s resources:

- It uses CUDA for computations and screen reading to perform actions.
- Make sure your CPU and GPU are capable of handling both the game and the script simultaneously.

If your hardware struggles to run Dead by Daylight smoothly without this script, **do not proceed** until you upgrade your system. 🚫🚀

---

## Troubleshooting

🛠️ **Common Issues & Fixes**:

1. **CUDA Errors**: Reinstall CUDA using the [official download link](https://developer.nvidia.com/cuda-downloads).
2. **Driver Issues**: Always reinstall your NVIDIA driver and reboot your PC after installing the script dependencies.
3. **ReShade Conflicts**: Use the `-dx12` launch option and reinstall your driver to resolve shader-related problems.

---

Happy farming! 🎮🌱 If you encounter further issues, open an issue on the GitHub repository for support.

---