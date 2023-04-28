function initialize(box)
	
	-- Experiment parameters 
	Duration =  tonumber(box:get_setting(2))
	Up_Time =  tonumber(box:get_setting(3))
	Between_Time =  tonumber(box:get_setting(4))
	Padding_Time =  tonumber(box:get_setting(5))
	
	PA =  tonumber(box:get_setting(6))
	PAX =  tonumber(box:get_setting(7))
	PBX =  tonumber(box:get_setting(8))

	-- Stim values
	A_Stim = 33024 
	B_Stim = 33025
	X_Stim = 33026
	Y_Stim = 33027
	Hide_Stim = 33028
	
	Stim_1 = 33031
	Stim_2 = 33032
	Stim_3 = 33033
	Stim_4 = 33034
	Stim_5 = 33035
	End_Stim = 33036
	
	Stop_Stim = 33029
	Start_Stim = 33030

	Experiment_Stop = 32770 
	Experiment_Start = 32769

	Experiment_Close = 1010

end

function process(box)

	local t = 0
	local past = 0
	math.randomseed(os.time())
	-- manages Before Experiment

	t = t + 1
	
	for i = 4, 0, -1 do
    		box:send_stimulation(1, (Stim_1 + i) , t, 0)
		box:send_stimulation(1, Hide_Stim, t+1, 0)
		t = t + 1.5
	end

	

	-- manages Start of Experiment
	Start_Time = t
	box:send_stimulation(1, Experiment_Start, Start_Time , 0)
	t = t + Padding_Time

	-- Manage all stimulus 
	while(t<Duration + Start_Time + Padding_Time)
	do
		box:send_stimulation(1, Start_Stim, t-Padding_Time/2, 0)

		-- STIM 1
		p = math.random() 
		if(p<=PA) --proba P(A)
		then
			box:send_stimulation(1, A_Stim, t, 0)
			box:send_stimulation(1, Hide_Stim, t+Up_Time, 0)
			past = 0
		else
			box:send_stimulation(1, B_Stim, t, 0)
			box:send_stimulation(1, Hide_Stim, t+Up_Time, 0)
			past = 1
		end
		t = t + Up_Time + Between_Time

		-- STIM 2 
		p = math.random() 
		if(past==0) 
		then
			if(p<=PAX) --proba P(X|A)
			then
				box:send_stimulation(1, X_Stim, t, 0)
				box:send_stimulation(1, Hide_Stim, t+Up_Time, 0)
			else
				box:send_stimulation(1, Y_Stim, t, 0)
				box:send_stimulation(1, Hide_Stim, t+Up_Time, 0)
			end
		else
			if(p<=PBX) --proba P(X|B)
			then
				box:send_stimulation(1, X_Stim, t, 0)
				box:send_stimulation(1, Hide_Stim, t+Up_Time, 0)
			else
				box:send_stimulation(1, Y_Stim, t, 0)
				box:send_stimulation(1, Hide_Stim, t+Up_Time, 0)
			end
		end
		
		t = t + Up_Time + Between_Time
		
		box:send_stimulation(1, Stop_Stim, t+Padding_Time/2, 0)

		t = t + Padding_Time
	end



	-- Manage End of experiment
	box:send_stimulation(1, Experiment_Stop, t, 0)
	t = t + 0.5

	box:send_stimulation(1, (End_Stim) , t, 0)
	box:send_stimulation(1, Hide_Stim, t+1, 0)
	t = t + 1.5

	box:send_stimulation(1, Experiment_Close, t, 0)

	

end