import time
def follow(thefile):
	thefile.seek(0,2)
	while True:
		line = thefile.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line

if __name__ == '__main__':
	logfile = open("C:/Users/anshu/AppData/LocalLow/Mediatonic/FallGuys_client/Player.log","r")
	loglines = follow(logfile)
	print("running")
	state = None
	scene = None
	for line in loglines:
		if "\"state\":" in line:
			state = line.strip().split(": ")[-1]
		elif "[ClientGameSession] NumPlayersAchievingObjective=0" in line:
			state = "started"
		elif "SquadManager::GetSquadScore squadId" in line:
			state = "ended"

		if "[StateGameLoading] Loading game level scene" in line:
			scene = line.split("scene")[-1].strip()
		# if "squad" in line:
		print("state",state,"\t","scene",scene,"\t\t\t",line.strip())
			# state started    scene None                      23:21:02.222: SquadManager::GetSquadScore squadId0 not found return 0