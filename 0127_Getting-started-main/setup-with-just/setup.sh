#run setup1.sh
./setup1.sh

#To avoid needing to manually restart the terminal after setup1.sh completes the code below creates a new terminal window
#and executes setup2.sh and setup3.sh in this new window
currentDirectory="$(pwd)"

osascript - "${currentDirectory}" <<EOF 
on run {currentDirectory}
  tell application "Terminal"
    do script "cd " & (quoted form of currentDirectory) & " && ./setup2.sh" 
    delay 90
    do script "cd " & (quoted form of currentDirectory) & " && ./setup3.sh" 
  end tell
end run
EOF
