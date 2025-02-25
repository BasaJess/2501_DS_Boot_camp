sudo apt-get update
sudo apt-get upgrade

#run setup1.sh
$CURRENT_PATH="$PWD"
gnome-terminal -- sh -c "bash -c \'$CURRENT_PATH/setup_linux1.sh; exec bash\'"
sleep 90
gnome-terminal -- sh -c "bash -c \'$CURRENT_PATH/setup_linux2.sh; exec bash\'"
sleep 90
gnome-terminal -- sh -c "bash -c \'$CURRENT_PATH/setup_linux3.sh; exec bash\'"


