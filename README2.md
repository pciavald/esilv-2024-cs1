# **5-Day Computer Science Bootcamp for Engineers**

*Welcome to the jungle! Get ready to dance with the Python and embark on a GUIde to making something useful. This 5-day bootcamp is designed to give you a survival kit in Linux, an introduction to programming, and the basics of user interface development—all while keeping things fun and engaging.*

**Schedule:** Each day runs from **09:00 to 12:00** and **13:00 to 17:00**, totaling **7 hours** per day.

---

## **Day 1 (Monday): Into the Wild—Computers and Operating Systems**

### **Morning Session (09:00 - 12:00)**

### **1. Welcome and Bootcamp Overview** *(15 minutes)*

- **Objectives:**
  - Introduce the bootcamp's structure with a flair of adventure.
  - Set expectations and get everyone excited for the week ahead.

### **2. What's a Computer?** *(2 hours 45 minutes)*

#### **2.1 The Processor: Architecture and Instruction Sets** *(45 minutes)*

- **Key Points:**
  - The CPU's role as the brain of the computer—no neurology degree required.
  - Basic fetch-decode-execute cycle—how the CPU takes commands and makes magic happen.
  - Introduction to the Instruction Pointer (EIP) and how it keeps the CPU on track.
  - CPUs vs. GPUs: Why your graphics card can't do your taxes (yet).

- **Notes:**

  - **Von Neumann Architecture (1945):**
    - **Components:**
      - **Control Unit (CU):** Directs the operation of the processor.
      - **Arithmetic Logic Unit (ALU):** Performs arithmetic and logical operations.
      - **Memory Unit:** Stores data and instructions.
      - **Input/Output (I/O):** Interfaces for peripherals.
    - **Registers:**
      - Small, fast storage locations within the CPU.
      - Store instructions, data, and memory addresses.
    - **Buses:**
      - **Data Bus:** Transfers actual data.
      - **Address Bus:** Carries information about where data should go.
      - **Control Bus:** Carries control signals from the CPU.

  - **Clock:**
    - Measures the speed at which a CPU executes instructions.
    - Clock speed measured in GHz (gigahertz)—billions of cycles per second.
    - Synchronizes the operations of the CPU.

  - **Fetch-Decode-Execute Cycle:**
    - **Program Counter (Instruction Pointer):** Points to the next instruction in memory.
    - **Control Unit Operations:**
      - **Fetch:** Retrieves the next instruction from memory.
      - **Decode:** Determines what the instruction means.
      - **Execute:** Performs the instruction using the ALU if necessary.
      - **Increment Program Counter:** Moves to the next instruction.

  - **Machine Code and Instruction Sets:**
    - **Machine Code:** Binary code that the CPU can execute directly.
    - **Assembly Language:** Low-level programming language using mnemonics.
      - Easier for humans to read but still corresponds closely to machine code.
    - **Instruction Sets:**
      - **x86 (Intel 8086, 1978):**
        - **CISC (Complex Instruction Set Computer):**
          - Large set of instructions, some complex.
          - Designed to reduce the number of instructions per program.
      - **ARM:**
        - **RISC (Reduced Instruction Set Computer):**
          - Smaller, highly optimized set of instructions.
          - Emphasizes efficiency and speed.
        - Widely used in mobile devices due to power efficiency.
      - **RISC-V:**
        - Open-source RISC architecture.
        - Allows for customization and extensions.

#### **2.2 Storage** *(30 minutes)*

- **Key Points:**
  - HDDs vs. SSDs: One spins, one doesn't, both hold your memes.
  - How data is stored and why you should care about read/write speeds.
  - The joy of waiting for a file to load—or not.

- **Notes:**

  - **Types of Storage Devices:**
    - **Hard Disk Drives (HDDs):**
      - Use spinning magnetic platters to store data.
      - Read/write head moves over the platters to access data.
      - Advantages:
        - Larger storage capacities at a lower cost per GB.
        - Suitable for storing large amounts of data.
      - Disadvantages:
        - Slower read/write speeds due to mechanical movement.
        - More susceptible to physical damage (e.g., drops).
    - **Solid State Drives (SSDs):**
      - Use flash memory (NAND) with no moving parts.
      - Data accessed electronically.
      - Advantages:
        - Faster read/write speeds—significantly improves system performance.
        - More durable and shock-resistant.
        - Quieter operation and lower power consumption.
      - Disadvantages:
        - Higher cost per GB compared to HDDs.
        - Limited number of write cycles (though significantly high).
  - **Storage Interfaces:**
    - **SATA (Serial ATA):**
      - Common interface for connecting storage devices.
      - SATA III supports up to 6 Gbps transfer speeds.
    - **NVMe (Non-Volatile Memory Express):**
      - Designed specifically for SSDs.
      - Uses PCIe lanes for faster data transfer (up to 32 Gbps or more).
      - Reduces latency and increases input/output operations per second (IOPS).
  - **Data Storage Concepts:**
    - **Blocks and Sectors:**
      - Data is stored in blocks (HDDs) or pages (SSDs).
      - Smallest unit of storage that can be read or written.
    - **File Systems:**
      - Organize how data is stored and retrieved.
      - Common file systems: NTFS, FAT32, exFAT, ext4.
  - **Importance of Read/Write Speeds:**
    - Affects system boot times, application loading, and file transfers.
    - Crucial for performance-intensive tasks like video editing, gaming, and database management.
  - **Storage Capacity Considerations:**
    - Balancing the need for speed with the need for storage space.
    - Common setup: Use an SSD for the operating system and frequently used applications, and an HDD for storing large files.

#### **2.3 RAM** *(30 minutes)*

- **Key Points:**
  - RAM: The computer's short-term memory (no goldfish jokes here).
  - How RAM affects multitasking—why 100 browser tabs might slow you down.
  - Difference between RAM and storage: One forgets, one forgives.

- **Notes:**

  - **Random Access Memory (RAM):**
    - Volatile memory used to store data and instructions temporarily.
    - Data is lost when power is turned off.
    - Allows for quick read/write access by the CPU.
  - **Types of RAM:**
    - **DRAM (Dynamic RAM):** Needs to be refreshed periodically.
    - **SRAM (Static RAM):** Faster and more expensive, used for cache memory.
    - **DDR (Double Data Rate) SDRAM:** Common in modern systems (DDR3, DDR4, DDR5).
  - **Role of RAM in System Performance:**
    - Holds the data and programs currently in use.
    - More RAM allows for more programs to run simultaneously.
    - Insufficient RAM leads to using virtual memory (swap space), which is slower.
  - **Memory Channels:**
    - Single, dual, triple, and quad-channel configurations.
    - Multiple channels increase data transfer rates between RAM and CPU.
  - **Impact on Multitasking:**
    - Enables smoother performance when running multiple applications.
    - Prevents system slowdowns and crashes due to memory overload.
  - **RAM vs. Storage:**
    - **RAM:**
      - Temporary storage for active processes.
      - Much faster access times.
      - Volatile—data is lost when power is off.
    - **Storage (HDD/SSD):**
      - Permanent storage for files and applications.
      - Slower access times compared to RAM.
      - Non-volatile—data persists after power off.

#### **2.4 PCI and Peripheral Devices** *(30 minutes)*

- **Key Points:**
  - What is PCI? Think of it as the computer's expansion slot for new gadgets—because who doesn't like upgrades?
  - Common devices: Network cards, sound cards—your computer's favorite accessories.
  - How peripherals communicate with the CPU—it's all about connecting the dots.

- **Notes:**

  - **Peripheral Component Interconnect (PCI):**
    - A hardware bus used for adding internal components to a desktop computer.
    - Allows for attachment of hardware devices in a standardized form.
  - **PCI Express (PCIe):**
    - Successor to PCI with higher bandwidth and speed.
    - Uses serial communication, offering multiple lanes (x1, x4, x8, x16).
    - Commonly used for graphics cards, SSDs, network cards.
  - **Common Peripheral Devices:**
    - **Graphics Cards (GPUs):**
      - Offload rendering of images, video, and animations.
      - Essential for gaming, video editing, and 3D rendering.
    - **Network Interface Cards (NICs):**
      - Provide wired or wireless network connectivity.
      - Can offer advanced features like higher speeds (10Gbps) or specialized networking.
    - **Sound Cards:**
      - Enhance audio output and input capabilities.
      - Useful for professional audio production.
    - **Capture Cards:**
      - Allow for recording input from external devices (e.g., game consoles).
  - **Communication with the CPU:**
    - Peripherals communicate via buses (PCIe lanes) to the motherboard chipset and CPU.
    - **Device Drivers:**
      - Software that allows the operating system to interact with hardware devices.
      - Essential for the proper functioning of peripherals.
  - **Plug and Play (PnP):**
    - Technology that allows the operating system to recognize and configure hardware automatically.
    - Simplifies the installation of new devices.
  - **Expansion and Upgrades:**
    - PCIe slots enable users to upgrade their systems by adding new capabilities.
    - Flexibility to customize the computer based on specific needs.

### **Lunch Break (12:00 - 13:00)**

### **Afternoon Session (13:00 - 17:00)**

### **3. Operating Systems Overview** *(2 hours)*

#### **3.1 Windows: The Good, the Bad, and the Ugly** *(45 minutes)*

- **The Good:**
  - **Wide Availability:** Like coffee shops, Windows is everywhere.
  - **Software Support:** Runs a vast array of applications—from AAA games and Adobe Creative Suite to niche professional software.
  - **Compatibility with Legacy Systems:** Your old software feels right at home.

- **The Bad:**
  - **Viruses:** Windows catches more bugs than a swamp in summer.
  - **Bugs and Glitches:** Ever seen the Blue Screen of Death? It's not a metal band.
  - **Dubious Architecture Choices:** Sometimes, even Windows doesn't know what Windows is doing.

- **The Ugly:**
  - **Spying:** Big Brother might be watching—you didn't need privacy, did you?

- **Notes:**

  - **Overview:**
    - Developed by Microsoft; most widely used desktop OS.
    - Known for its graphical user interface and user-friendly design.
  - **Strengths:**
    - **Extensive Software Library:**
      - Supports a wide range of applications, including industry-standard software like Microsoft Office, Adobe Suite, and various engineering tools.
      - Preferred platform for gaming due to DirectX support.
    - **Hardware Compatibility:**
      - Supports a vast array of hardware components and peripherals.
      - Regular driver updates from manufacturers.
    - **Enterprise Features:**
      - Active Directory, group policies, and other tools for corporate environments.
  - **Weaknesses:**
    - **Security Vulnerabilities:**
      - Targeted frequently by malware, viruses, and ransomware.
      - Requires regular updates and antivirus software for protection.
    - **System Stability:**
      - Susceptible to crashes and system errors (e.g., Blue Screen of Death).
    - **Resource Intensive:**
      - Can be heavy on system resources, leading to slower performance on older hardware.
  - **Privacy Concerns:**
    - Telemetry data collection and user tracking.
    - Concerns over how user data is used and stored.
  - **User Experience:**
    - Frequent updates and forced restarts can be disruptive.
    - The interface changes between versions (e.g., Windows 7 to Windows 10) can be jarring for users.

#### **3.2 macOS is BSD: Story of a Monolith** *(30 minutes)*

- **Key Points:**
  - macOS roots in BSD Unix—Apple didn't fall far from the tree.
  - The elegance of integration—when hardware and software finish each other's sentences.
  - Limitations: You can have any color you like, as long as it's space gray.

- **Notes:**

  - **Overview:**
    - Developed by Apple Inc. for Macintosh computers.
    - Built upon a Unix foundation (specifically BSD Unix), providing a stable and secure environment.
  - **Strengths:**
    - **Hardware and Software Integration:**
      - Tight integration leads to optimized performance and reliability.
      - Seamless experience across Apple devices (iPhone, iPad, Mac).
    - **User Interface and Experience:**
      - Clean, intuitive interface with emphasis on aesthetics.
      - Consistent design language across applications.
    - **Built-in Applications:**
      - Comes with a suite of productivity and creative tools (e.g., Pages, Keynote, GarageBand).
    - **Security and Stability:**
      - Less targeted by malware compared to Windows.
      - Stable Unix-based core.
  - **Weaknesses:**
    - **Closed Ecosystem:**
      - Limited customization options compared to other operating systems.
      - Hardware upgrades are often restricted.
    - **Software Compatibility:**
      - Some software and games are not available or optimized for macOS.
    - **Cost:**
      - Apple hardware tends to be more expensive.
    - **Limited Hardware Choices:**
      - Users must choose from Apple's product lineup with few options for customization.
  - **Developer Environment:**
    - Terminal access to Unix tools.
    - Preferred by many developers for its Unix base and support for programming languages.

#### **3.3 The World of Linux** *(45 minutes)*

- **Key Points:**
  - Linux: The open-source underdog that's everywhere.
  - Distributions galore—Ubuntu, Fedora, Debian—collect them all!
  - Customization: Linux is like Lego for your computer.
  - **Where Linux Falls Short:** Despite its strengths, Linux can lack support for certain proprietary software and games, making it less ideal for some users. It also often requires getting your hands dirty to drill down into issues, but there is almost always a way out of any issue.

- **Notes:**

  - **Overview:**
    - Open-source operating system based on Unix principles.
    - Kernel developed by Linus Torvalds in 1991.
    - Widely used in servers, embedded systems, and increasingly on desktops.
  - **Distributions (Distros):**
    - **Ubuntu:** User-friendly, popular for desktops and beginners.
    - **Fedora:** Cutting-edge technologies, sponsored by Red Hat.
    - **Debian:** Known for stability and vast software repositories.
    - **Arch Linux:** For advanced users who prefer customization.
    - Each distro can have different package managers, desktop environments, and philosophies.
  - **Strengths:**
    - **Open Source:**
      - Free to use, modify, and distribute.
      - Community-driven development ensures rapid updates and bug fixes.
    - **Customization:**
      - Users can modify nearly every aspect of the system.
      - Choice of desktop environments (GNOME, KDE, XFCE, etc.).
    - **Performance and Efficiency:**
      - Can run on a wide range of hardware, including older systems.
      - Lightweight distros available for minimal resource usage.
    - **Security:**
      - Less targeted by malware.
      - Strong security practices due to open-source scrutiny.
  - **Weaknesses:**
    - **Software Compatibility:**
      - Some proprietary software and games are unavailable or have limited support.
      - Workarounds like Wine or virtual machines can be used but may not be perfect.
    - **Learning Curve:**
      - May require command-line usage for certain tasks.
      - Troubleshooting can be more complex and require technical knowledge.
    - **Hardware Compatibility:**
      - Potential issues with drivers for certain hardware components.
      - Community or open-source drivers may lack full functionality.
  - **Community and Support:**
    - Extensive online forums, wikis, and communities for support.
    - Documentation can vary in quality between distros.
  - **Use Cases:**
    - Ideal for servers, development environments, and users who prefer customization.
    - Widely used in supercomputing, IoT devices, and Android smartphones (Linux kernel).

### **4. Linux Architecture** *(2 hours)*

#### **4.1 The Kernel and Userland** *(30 minutes)*

- **Key Points:**
  - Kernel: The bouncer of your system—decides who gets in.
  - Userland: Where all the apps hang out.
  - Interaction between hardware and software—making the magic happen.

- **Notes:**

  - **Linux Kernel:**
    - Core component of the operating system.
    - Manages system resources and hardware communication.
    - Handles memory management, process scheduling, device drivers, and system security.
  - **Userland (User Space):**
    - Area where user processes run.
    - Includes all applications and libraries that interact with the kernel via system calls.
    - Examples: Shells (bash, zsh), graphical interfaces, user applications.
  - **System Calls:**
    - Interface between user applications and the kernel.
    - Allows programs to request services from the kernel (e.g., file operations, network communication).
  - **Modules and Drivers:**
    - Kernel modules can be loaded or unloaded to add functionality (e.g., support for new hardware).
    - Device drivers facilitate communication between the kernel and hardware devices.
  - **Monolithic vs. Microkernel:**
    - **Monolithic Kernel:**
      - All system services run in kernel space.
      - Linux uses a monolithic kernel with modular capabilities.
    - **Microkernel:**
      - Minimal kernel handling basic services; other services run in user space.
      - Pros and cons in terms of performance and stability.
  - **Interaction Flow:**
    - User interacts with applications in user space.
    - Applications make system calls to the kernel.
    - Kernel interacts with hardware and returns responses to user space.

#### **4.2 File-Based System and UNIX Directories** *(30 minutes)*

- **Key Points:**
  - Everything is a file—even your keyboard, sort of.
  - Navigating the filesystem: Why root is not just for plants.
  - Common directories: `/home` is where the heart is.

- **Notes:**

  - **Filesystem Hierarchy Standard (FHS):**
    - Defines the directory structure and directory contents in Unix-like operating systems.
  - **Everything is a File:**
    - Devices, processes, and system information are represented as files.
    - Allows for a consistent interface for interaction.
  - **Key Directories:**
    - **`/` (Root):**
      - The top of the directory tree.
      - All other directories branch from here.
    - **`/bin`:**
      - Essential command binaries (e.g., `ls`, `cp`, `mv`).
    - **`/boot`:**
      - Static files required for booting the system (e.g., kernel).
    - **`/dev`:**
      - Device files representing hardware components (e.g., `/dev/sda`).
    - **`/etc`:**
      - System configuration files.
    - **`/home`:**
      - User home directories (e.g., `/home/username`).
    - **`/lib` and `/lib64`:**
      - Essential shared libraries and kernel modules.
    - **`/media` and `/mnt`:**
      - Mount points for removable media and temporary mounts.
    - **`/opt`:**
      - Optional application software packages.
    - **`/proc`:**
      - Virtual filesystem providing process and system information.
    - **`/root`:**
      - Home directory for the root user.
    - **`/sbin`:**
      - System administration binaries (e.g., `fdisk`, `ifconfig`).
    - **`/tmp`:**
      - Temporary files (often cleared on reboot).
    - **`/usr`:**
      - User utilities and applications.
      - Subdirectories like `/usr/bin`, `/usr/lib`, `/usr/share`.
    - **`/var`:**
      - Variable files like logs, databases, email spool files.
  - **Mount Points and Devices:**
    - Storage devices are mounted to directories.
    - Example: Mounting a USB drive to `/media/usb`.
  - **Permissions and Ownership:**
    - Files and directories have permissions and ownership attributes.
    - Important for system security and user access control.

#### **4.3 Permissions, Groups, and Owners** *(30 minutes)*

- **Key Points:**
  - Users and groups: It's like social media for files.
  - File permissions: Read, write, execute—permissions so important, they deserve their own rules.
  - Changing permissions: Use `chmod` and `chown` to manage access.

- **Notes:**

  - **Users and Groups:**
    - **Users:**
      - Individual accounts with unique User IDs (UIDs).
      - Each user has a home directory and specific permissions.
    - **Groups:**
      - Collections of users.
      - Used to manage permissions for multiple users simultaneously.
  - **File Ownership:**
    - Every file and directory has an owner (user) and a group.
    - Ownership determines access rights.
  - **Permissions:**
    - **Read (r):** Permission to read the file or list directory contents.
    - **Write (w):** Permission to modify the file or directory.
    - **Execute (x):** Permission to execute a file or traverse a directory.
  - **Permission Categories:**
    - **User (u):** The owner of the file.
    - **Group (g):** Users who are members of the file's group.
    - **Others (o):** All other users.
  - **Viewing Permissions:**
    - Use `ls -l` to list files with permissions.
    - Permissions are displayed as a string (e.g., `-rwxr-xr--`).
  - **Changing Permissions:**
    - **`chmod`:**
      - Change the permissions of a file or directory.
      - Syntax: `chmod [options] mode file`.
      - Modes can be symbolic (e.g., `chmod u+x file`) or numeric (e.g., `chmod 755 file`).
    - **Numeric Representation:**
      - Each permission has an associated number:
        - Read = 4
        - Write = 2
        - Execute = 1
      - Sum the numbers for each category.
      - Example: `chmod 755 file` sets permissions to `rwxr-xr-x`.
  - **Changing Ownership:**
    - **`chown`:**
      - Change the owner and/or group of a file or directory.
      - Syntax: `chown [options] user[:group] file`.
      - Requires superuser privileges.
  - **Special Permissions:**
    - **Setuid and Setgid Bits:**
      - Allow users to execute a file with the permissions of the file owner or group.
    - **Sticky Bit:**
      - On directories, restricts file deletion within the directory.

#### **4.4 Command Line Basics** *(30 minutes)*

- **Key Points:**
  - Terminal vs. shell vs. console—when words get confusing.
  - Basic commands: `ls`, `cd`, `pwd`—the holy trinity.
  - Standard input/output: Talk to your computer without emojis.

- **Notes:**

  - **Definitions:**
    - **Terminal Emulator:**
      - Software application that emulates a video terminal within another display architecture.
      - Examples: GNOME Terminal, Konsole, xterm.
    - **Shell:**
      - Command-line interpreter that provides a user interface for access to the operating system's services.
      - Examples: Bash, Zsh, Fish.
    - **Console:**
      - Physical terminal or a virtual console accessible via Ctrl+Alt+F1-F6.
  - **Navigating the Filesystem:**
    - **`pwd` (Print Working Directory):**
      - Displays the current directory path.
    - **`ls` (List):**
      - Lists files and directories in the current directory.
      - Options:
        - `-l`: Long listing format.
        - `-a`: Include hidden files (those starting with `.`).
    - **`cd` (Change Directory):**
      - Changes the current working directory.
      - Usage: `cd /path/to/directory`.
      - `cd ..` moves up one directory level.
  - **File Manipulation Commands:**
    - **`touch`:**
      - Creates an empty file or updates the timestamp of an existing file.
    - **`mkdir`:**
      - Creates a new directory.
    - **`rm`:**
      - Removes files or directories.
      - Use `rm -r` to remove directories recursively.
      - **Caution:** No recycle bin—deleted files are gone.
    - **`cp`:**
      - Copies files or directories.
      - Use `-r` to copy directories recursively.
    - **`mv`:**
      - Moves or renames files or directories.
  - **Standard Input/Output (I/O):**
    - **Standard Input (stdin):**
      - Data input stream, default is keyboard input.
    - **Standard Output (stdout):**
      - Data output stream, default is the terminal display.
    - **Standard Error (stderr):**
      - Output stream for error messages.
    - **Redirection:**
      - `>` redirects stdout to a file (overwrites).
      - `>>` appends stdout to a file.
      - `<` redirects stdin from a file.
      - `2>` redirects stderr.
    - **Pipes (`|`):**
      - Passes the output of one command as input to another.
      - Example: `ls | grep 'txt'` filters `ls` output for lines containing 'txt'.
  - **Command-Line Editing and History:**
    - Use arrow keys to navigate command history.
    - Tab completion for commands and file names.
    - **Aliases:**
      - Shortcuts for commands.
      - Set in shell configuration files (e.g., `.bashrc`).

### **4.4 Command Line Basics (continued)** *(30 minutes)*

- **Key Points (continued):**
  - **Searching and Filtering:**
    - **`grep`:** Searches for patterns within files.
      - Example: `grep "error" logfile.txt` looks for the word "error" in the file `logfile.txt`.
      - Can be combined with other commands using pipes (e.g., `ps aux | grep "python"`).
    - **`find`:** Locates files and directories based on name or other attributes.
      - Example: `find /home -name "*.txt"` searches for all `.txt` files under `/home`.
    - **`wc`:** Word count, line count, and character count.
      - Example: `wc -l myfile.txt` counts the number of lines in `myfile.txt`.
    - **`head` and `tail`:** View the start or end of a file.
      - Example: `head -n 10 myfile.txt` displays the first 10 lines.
      - `tail -f logfile.txt` allows real-time monitoring of a file as new lines are appended (useful for logs).
    - **`cut` and `awk`:** Extract fields from text.
      - Example: `cut -d':' -f1 /etc/passwd` extracts the first field (delimited by `:`).
    - **`sort` and `uniq`:** Sorting and removing duplicates from text.
      - Example: `sort myfile.txt | uniq` sorts the file and removes duplicate lines.
  - **Working with Environment Variables:**
    - **`env`:** Displays all environment variables.
    - **`export`:** Sets environment variables in the current shell session.
      - Example: `export PATH=$PATH:/new/path` adds `/new/path` to the system’s `PATH`.
    - **`echo`:** Displays the value of variables or text.
      - Example: `echo $PATH` shows the current `PATH` variable.

---

## **Day 2 (Tuesday): Surviving in the Linux Wilderness**

### **Morning Session (09:00 - 12:00)**

### **1. Setting Up Camp: Creating a Debian Virtual Machine** *(1 hour)*

- **Activities:**
  - Install VirtualBox or your virtualization tool of choice.
  - Step-by-step guide to installing Debian.
  - Configuring settings: Allocating resources (RAM, disk space), setting up network access.
  - Installing guest additions for better performance.

---

### **2. Navigating the Command Line Jungle** *(2 hours)*

#### **2.1 File and Directory Operations** *(1 hour)*

- **Commands:**
  - **Navigating and Listing:**
    - **`ls`, `cd`, `pwd`**—Recap of basic navigation.
  - **File and Directory Management:**
    - **`mkdir`, `rmdir`:** Creating and removing directories.
    - **`rm`, `mv`, `cp`:** Removing, moving, and copying files.
  - **Viewing and Editing Files:**
    - **`cat`, `more`, `less`:** View file contents.
    - **`nano`, `vim`:** Basic text editing within the terminal.

#### **2.2 Text Processing and Utilities** *(1 hour)*

- **Commands:**
  - **`grep`, `find`, `cut`, `awk`:** Searching and filtering.
  - **`wc`, `head`, `tail`:** Counting lines, showing file heads/tails.
  - **`sort`, `uniq`:** Sorting text, removing duplicates.
  - **`diff` and `cmp`:** Compare files.
  - **`chmod`, `chown`:** Permissions and ownership (recap).

---

### **Lunch Break (12:00 - 13:00)**

---

### **Afternoon Session (13:00 - 17:00)**

### **3. Essential Linux Commands Continued** *(1 hour)*

#### **3.1 System Information and Monitoring** *(30 minutes)*

- **Commands:**
  - **`top` or `htop`:** Real-time process monitoring.
  - **`free`:** Memory usage.
  - **`df` and `du`:** Disk usage by files and directories.
  - **`uptime`:** System uptime and load average.
  - **`ps aux`:** Listing running processes with detailed information.

#### **3.2 Networking Commands** *(30 minutes)**

- **Commands:**
  - **`ping`:** Test network connectivity.
  - **`ifconfig` or `ip addr`:** Show network interfaces and IP addresses.
  - **`ssh`:** Securely connect to remote machines.
  - **`scp` and `rsync`:** Copy files between machines over SSH.
    - Example: `scp file.txt user@remote:/path/to/destination`.
    - **`rsync`:** Synchronize files and directories across machines, useful for backups.

---

### **4. Bash Is a Programming Language** *(2 hours)**

#### **4.1 Writing Simple Scripts** *(1 hour)**

- **Key Concepts:**
  - **Shell Scripting Basics:**
    - Starting a script with `#!/bin/bash`.
    - Using variables: `VAR="hello"`.
    - **Control Structures:**
      - **If Statements:** `if [ condition ]; then ... fi`.
      - **Loops:** `for i in {1..5}; do echo $i; done`.
      - **While Loops:** `while [ condition ]; do ... done`.
  - **Reading Input from the User:**
    - **`read`:** Captures user input.
      - Example: `read -p "Enter your name: " name; echo "Hello, $name!"`.

#### **4.2 Bash Project: Calendar Creator** *(1 hour)**

- **Activity:**
  - **Create a Bash Script:**
    - Generates a directory structure representing months of the year.
    - Inside each month, create a file for each day.
    - Each file contains the date and the corresponding day of the week.
    - Example: `cat ./2024/01/01.txt` outputs `2024-01-01 is a Monday`.

---

### **5. Git: Your Favorite Worst Nightmare** *(1 hour)**

#### **5.1 Version Control Basics** *(30 minutes)**

- **Key Points:**
  - **What is Git?:**
    - Distributed version control system for tracking changes in code.
  - **Repositories:**
    - Local vs. remote repositories (e.g., GitHub).
  - **Basic Commands:**
    - **`git init`:** Initialize a new Git repository.
    - **`git clone`:** Clone an existing repository.
    - **`git status`:** Check the status of your working directory.

#### **5.2 The Developer's Dance: Add, Commit, Push** *(30 minutes)**

- **Commands:**
  - **`git add`:** Stage changes for the next commit.
  - **`git commit`:** Save changes with a message describing what changed.
  - **`git push`:** Send changes to a remote repository.
  - **Tips:**
    - Clear commit messages make life easier later on.
    - Use branches to work on features independently before merging.

---

## **Day 3 (Wednesday): Dance with the Python**

### **Morning Session (09:00 - 12:00)**

### **1. Python Programming Fundamentals** *(3 hours)**

#### **1.1 Variables and Data Types** *(45 minutes)**

- **Key Points:**
  - **Variables:**
    - Dynamic typing in Python—no need to declare types.
    - Basic data types: `int`, `float`, `str`, `bool`.
  - **Lists and Dictionaries:**
    - Lists: Ordered collections.
    - Dictionaries: Key-value pairs.

#### **1.2 Control Structures** *(1 hour)**

- **Key Points:**
  - **Conditionals:**
    - `if`, `elif`, `else`: Making decisions.
    - Example: `if x > 10: print("x is greater than 10")`.
  - **Loops:**
    - **`for` and `while` loops** for iteration.
    - Example: `for i in range(5): print(i)`.

#### **1.3 Functions** *(45 minutes)**

- **Key Points:**
  - **Defining Functions:**
    - Use `def` to create reusable code blocks.
    - Accept parameters and return values.
    - Example: `def greet(name): return f"Hello, {name}"`.

---

### Lunch Break (12:00 - 13:00)

---

### **Afternoon Session (13:00 - 17:00)**

### **2. Practical Python Applications** *(2 hours)**

#### **2.1 Fast and Furious Hello World** *(30 minutes)**

- **Activity:**
  - Write a simple script to print `Hello, World!`.
  - Introduce basic input/output functions (`input()`).

#### **2.2 Reading Errors and Exception Management** *(30 minutes)**

- **Key Points:**
  - **Try/Except Blocks:** Handling errors gracefully.
  - **Common Exceptions:** `IndexError`, `KeyError`, `ValueError`.
  - Example: `try: ... except ValueError: print("That's not a number!")`.

#### **2.3 Fun Project: Build a Simple Encryption Program** *(1 hour)**

- **Activity:**
  - Create a Caesar cipher program.
  - Allow user input for the message and encryption shift.
  - Output