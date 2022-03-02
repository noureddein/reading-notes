# Practice in the Terminal

# The Command Line

**What is Command Line?**
- Command line or Terminal is atext based interface to the system.Writing commands in terminal will give us a feedback as a text.

- ```user@bash: ls -l /home/ryan ```
  __ls__: is the command.
  __-l__: command line arguments and it is optional.

**What is Shell?**
- __Shell__ is part of the operating system that defines how the terminal behave and looks after running the commands.
- Types of Shell:
  - __bash__: Bourne shell
  - __zsh__: Z shell

---

# Shortcuts 
> When entering commands they are saved in history, you can navigate them by using the Up and Down arrow keys.
> ```cd```: cd without arguments will take you to the home directory.
> **Tap**: hit tab for auto complete


---

# Basic Navigation

- To moving around the system we can use these commands line:
  - __pwd__: **Print working Directory** this command told us where we are now, what is the current or present directory.
  - __ls__: **List** this command told us what this directory contain (Files and Folders).
    - **ls  [option] [location]**: Ex: __ls -l__

> Paths:
  - The file system under Linux is hierarchical structure, the very top of the structure is what is called **root** directory its denoted by a single slash **(/)**
>> * Absolute Paths: They specify a location in relation to the root directory, they start with forward slash **(/)**.
>> * Relative Paths:They specify a location in relation to where we currently are in the system, they will not begin with a forward slash.

> More on Paths:
>> - ```~ (tilde)```: shortcut for home directory
>> - ``` .(dot) ```: this is a reference to the current directory.
>> - ``` ..(dotdot) ```: this is a reference to the parent directory.

---

# More About Files

  * Everything is a file in Linux, text, directory, keyboard, monitor all of them are files in Linux.
  * Linux is an *Extensionless System*, thats mean the linux do not care about the extension it can open the file even if the file do not have an extension.
  *  Linux is case sensitive. in Linux ```FILE1.txt File1.txt file1.TXT``` these files are different form each other.
  *  Space when naming fils in Linux are totally valid ```Holiday Photos```
  *  To access file that have a space, we should wrap it between quotes or we can use backslash to escape the space.

---

# Manual Pages

> The manual pages are a set of pages explain what the command do, the arguments it take.

  * To see what the command can do type ```man <command to look up>```


---

# File Manipulation

  * ```mkdir <direcrory_name>```:  use this command to create a new directory (new folder).
  * ```mkdir -p <direcrory_name>```: this command let us create a parent directory and a sub directory in one line.
  * ```rmdir <dir_name>```: this command for deleting directory.
  * ```touch <file_name>```: with this command we can create a blank file.
  * ```cp <source> <destination>```: use this command to copy a file or directory.
  * ```mv <source> <destination>```: use this command to move a file or directory.
  * ```rm <filename>```: to remove a file or an empty directory.
  * ```rm -f <filename>```:to remove a non-empty directory. 

---

Cheat Sheet link [Cheat Sheet](https://ryanstutorials.net/linuxtutorial/cheatsheetvi.php)
---

**[Go Back](./README.md)**

