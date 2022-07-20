//Maya ASCII 2022 scene
//Name: Script.ma
//Last modified: Wed, Jul 20, 2022 08:47:45 AM
//Codeset: 1252
requires maya "2022";
requires -nodeType "bifrostBoard" -nodeType "bifShape" -dataType "bifData" "bifrostGraph" "2.2.1.0-202102081428-b33b49f";
requires "mtoa" "4.2.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2022";
fileInfo "version" "2022";
fileInfo "cutIdentifier" "202102181415-29bfc1879c";
fileInfo "osv" "Windows 10 Pro for Workstations v2009 (Build: 22000)";
fileInfo "UUID" "88B932E3-486E-979F-D943-1AA9998397A1";
createNode transform -s -n "persp";
	rename -uid "318CDC81-4C5A-3F15-5355-958DD24823F3";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 19.687848447235432 11.572227496335639 24.662541779773584 ;
	setAttr ".r" -type "double3" -20.138352729602598 38.600000000000151 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "14035078-47A1-8469-C132-23AB58C53A34";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 33.612033451538025;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "E5740371-432D-9B67-175E-D0A34E81A2D0";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "768BEAA1-48DF-2C34-42C5-64A013DD17E5";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "7023A728-4694-305C-CD8B-BB9FDD342F33";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "D6724A30-4B86-3263-67BA-6E8EDF32B464";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "2F588D92-493E-891F-ADE4-559C67E68EDC";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "E03E5731-44CC-1CAA-4098-EF8CA4A3627B";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -n "rig_global";
	rename -uid "B8506198-45B2-1D45-D1E3-EF9414944348";
	addAttr -ci true -sn "data" -ln "data" -dt "string";
	addAttr -s false -ci true -sn "rig_global_input_network" -ln "rig_global_input_network" 
		-at "message";
	addAttr -s false -ci true -sn "rig_global_output_network" -ln "rig_global_output_network" 
		-at "message";
	setAttr ".data" -type "string" "cartoon";
createNode transform -n "rig_global_guides" -p "rig_global";
	rename -uid "EDA2CEC5-4C7E-CAA6-2DF6-20B804ACB8F7";
	addAttr -ci true -sn "data" -ln "data" -dt "string";
	addAttr -s false -ci true -sn "rig_global_guide_output_network" -ln "rig_global_guide_output_network" 
		-at "message";
	addAttr -s false -ci true -sn "rig_global_guide_input_network" -ln "rig_global_guide_input_network" 
		-at "message";
	setAttr ".data" -type "string" "cartoon_guides";
createNode transform -n "world_base_gd_0" -p "rig_global_guides";
	rename -uid "BB951BBC-4847-93A7-1BB8-0F8F705560E9";
createNode bifShape -n "world_base_gd_Shape0" -p "world_base_gd_0";
	rename -uid "47526127-4CAF-C5FB-05A0-10B7BAE00C62";
	setAttr -k off ".v";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "world_01_gd_0" -p "rig_global_guides";
	rename -uid "BB22DEDC-4140-827E-75D6-87A6843E8417";
createNode bifShape -n "world_01_gd_Shape0" -p "world_01_gd_0";
	rename -uid "968A8AA3-4CA0-9DDC-F7F8-C49CBA52D04A";
	setAttr -k off ".v";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "world_02_gd_0" -p "rig_global_guides";
	rename -uid "C40CE1C7-468B-B61E-3D70-87A7035230A2";
	setAttr ".t" -type "double3" 0 3 0 ;
createNode bifShape -n "world_02_gd_Shape0" -p "world_02_gd_0";
	rename -uid "AAD48BAE-44D4-6F15-2B20-99BD0537B885";
	setAttr -k off ".v";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "cog_01_gd_0" -p "rig_global_guides";
	rename -uid "C8233AC1-42C3-0065-BB2B-BB81A2FAA033";
	setAttr ".t" -type "double3" 0 3 0 ;
createNode bifShape -n "cog_01_gd_Shape0" -p "cog_01_gd_0";
	rename -uid "98110FB6-4F06-752A-4B13-AA96E8D71CA7";
	setAttr -k off ".v";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "setting_01_gd_0" -p "rig_global_guides";
	rename -uid "4DE7FDDB-4B42-6C14-DF7C-62A888E6CB3A";
	setAttr ".t" -type "double3" 0 3 0 ;
createNode bifShape -n "setting_01_gd_Shape0" -p "setting_01_gd_0";
	rename -uid "5AC7885F-454B-80FF-3086-32BD18C5AFD3";
	setAttr -k off ".v";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "rig_global_controls" -p "rig_global";
	rename -uid "C5958506-4145-7E70-7949-F59F0E6ADB7E";
	addAttr -ci true -sn "data" -ln "data" -dt "string";
	addAttr -s false -ci true -sn "rig_global_control_output_network" -ln "rig_global_control_output_network" 
		-at "message";
	addAttr -s false -ci true -sn "rig_global_control_input_network" -ln "rig_global_control_input_network" 
		-at "message";
	setAttr ".data" -type "string" "cartoon_controls";
createNode transform -n "World_01_ctrl_0" -p "rig_global_controls";
	rename -uid "62D1F044-40D2-F2F1-C5B7-24B84CD390E4";
createNode bifShape -n "World_01_ctrl_Shape0" -p "World_01_ctrl_0";
	rename -uid "6866E506-4688-ADD9-336B-4AA9D4B77A31";
	setAttr -k off ".v";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "World_02_ctrl_0" -p "rig_global_controls";
	rename -uid "F1840DF6-4051-CE6D-D5B8-3DA730BCF1FA";
createNode bifShape -n "World_02_ctrl_Shape0" -p "World_02_ctrl_0";
	rename -uid "78BEE984-4511-6FFD-975B-F287124B6D2B";
	setAttr -k off ".v";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "COG_ctrl_0" -p "rig_global_controls";
	rename -uid "59DE2708-4768-52FF-89F7-D8951E2EAB8C";
createNode bifShape -n "COG_ctrl_Shape0" -p "COG_ctrl_0";
	rename -uid "B441D770-4D88-DD50-F7E6-509777D66B2B";
	setAttr -k off ".v";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "Setting_ctrl_0" -p "rig_global_controls";
	rename -uid "B5329EBA-4F4C-D578-B0B8-E991397C6103";
createNode bifShape -n "Setting_ctrl_Shape0" -p "Setting_ctrl_0";
	rename -uid "A83CB5B2-4814-CA24-40E9-F38F4DD36A62";
	setAttr -k off ".v";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "rig_global_skeleton" -p "rig_global";
	rename -uid "3210BA47-4DFB-2103-DA5E-1E94A552A59C";
	addAttr -ci true -sn "data" -ln "data" -dt "string";
	addAttr -s false -ci true -sn "rig_global_skeleton_output_network" -ln "rig_global_skeleton_output_network" 
		-at "message";
	addAttr -s false -ci true -sn "rig_global_skeleton_input_network" -ln "rig_global_skeleton_input_network" 
		-at "message";
	setAttr ".data" -type "string" "cartoon_skeleton";
createNode joint -n "World_01_ctrl_0_jnt" -p "rig_global_skeleton";
	rename -uid "C3210AFC-42B0-A30D-0F35-1B85486CC4A0";
	addAttr -ci true -sn "data" -ln "data" -dt "string";
	addAttr -ci true -sn "rootJoint" -ln "rootJoint" -dt "string";
	setAttr ".it" no;
	setAttr -k on ".jox";
	setAttr -k on ".joy";
	setAttr -k on ".joz";
	setAttr ".data" -type "string" "";
createNode joint -n "World_02_ctrl_0_jnt" -p "World_01_ctrl_0_jnt";
	rename -uid "F03E2142-4EB6-A9D7-F4BB-7EAA4F2B7CF0";
	addAttr -ci true -sn "data" -ln "data" -dt "string";
	addAttr -ci true -sn "rootJoint" -ln "rootJoint" -dt "string";
	setAttr ".it" no;
	setAttr -k on ".jox";
	setAttr -k on ".joy";
	setAttr -k on ".joz";
	setAttr ".data" -type "string" "";
createNode joint -n "COG_ctrl_0_jnt" -p "World_02_ctrl_0_jnt";
	rename -uid "46E3534A-444A-F412-D50F-368719DB64F2";
	addAttr -ci true -sn "data" -ln "data" -dt "string";
	addAttr -ci true -sn "rootJoint" -ln "rootJoint" -dt "string";
	setAttr ".it" no;
	setAttr -k on ".jox";
	setAttr -k on ".joy";
	setAttr -k on ".joz";
	setAttr ".data" -type "string" "";
createNode joint -n "Setting_ctrl_0_jnt" -p "COG_ctrl_0_jnt";
	rename -uid "35A30615-4B94-7B1D-146F-4290B90DB9A4";
	addAttr -ci true -sn "data" -ln "data" -dt "string";
	addAttr -ci true -sn "rootJoint" -ln "rootJoint" -dt "string";
	setAttr ".it" no;
	setAttr -k on ".jox";
	setAttr -k on ".joy";
	setAttr -k on ".joz";
	setAttr ".data" -type "string" "";
createNode transform -n "rig_global_misc" -p "rig_global";
	rename -uid "45467BEE-4CCC-8EAB-04EB-17BE7D878CCB";
	addAttr -ci true -sn "data" -ln "data" -dt "string";
	addAttr -s false -ci true -sn "rig_global_misc_output_network" -ln "rig_global_misc_output_network" 
		-at "message";
	addAttr -s false -ci true -sn "rig_global_misc_input_network" -ln "rig_global_misc_input_network" 
		-at "message";
	setAttr ".data" -type "string" "cartoon_misc";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "0EF73C76-46A8-9D34-7D55-7CA79ABFA13E";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "31148165-4CF1-49EC-A3BE-76B14EAF7C25";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "C7F8243A-4C60-779F-1BD6-E8B71E5BE199";
createNode displayLayerManager -n "layerManager";
	rename -uid "C3DC25C9-4043-03B8-7A86-CFBAED1E8639";
createNode displayLayer -n "defaultLayer";
	rename -uid "EC510E9C-4C0D-9AA7-D275-1AA4396CBB30";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "D1B8DFCC-4FBF-5068-6593-3BA821267DB5";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "CA7ECF74-43C5-DD4E-0C79-E696E4E089D1";
	setAttr ".g" yes;
createNode network -n "rig_global_input_network";
	rename -uid "A99C4C1B-48AC-96B8-C190-83BE46761FB5";
	addAttr -s false -ci true -sn "rig_global_input_network" -ln "rig_global_input_network" 
		-at "message";
createNode network -n "rig_global_output_network";
	rename -uid "65BEE39C-4EAF-55E4-0217-EE8F1708690A";
	addAttr -s false -ci true -sn "rig_global_output_network" -ln "rig_global_output_network" 
		-at "message";
createNode network -n "rig_global_guide_input_network";
	rename -uid "2A4A292F-457E-5FBA-55A0-0C99CEA0D3AE";
	addAttr -s false -ci true -sn "rig_global_guide_input_network" -ln "rig_global_guide_input_network" 
		-at "message";
createNode network -n "rig_global_guide_output_network";
	rename -uid "75CF398D-425C-6B86-982A-E7B47ACBD5C8";
	addAttr -s false -ci true -sn "rig_global_guide_output_network" -ln "rig_global_guide_output_network" 
		-at "message";
	addAttr -ci true -sn "world_base_gd_0_worldMatrix" -ln "world_base_gd_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "world_base_gd_0_worldInverseMatrix" -ln "world_base_gd_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "world_01_gd_0_worldMatrix" -ln "world_01_gd_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "world_01_gd_0_worldInverseMatrix" -ln "world_01_gd_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "world_02_gd_0_worldMatrix" -ln "world_02_gd_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "world_02_gd_0_worldInverseMatrix" -ln "world_02_gd_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "cog_01_gd_0_worldMatrix" -ln "cog_01_gd_0_worldMatrix" -dt "matrix";
	addAttr -ci true -sn "cog_01_gd_0_worldInverseMatrix" -ln "cog_01_gd_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "setting_01_gd_0_worldMatrix" -ln "setting_01_gd_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "setting_01_gd_0_worldInverseMatrix" -ln "setting_01_gd_0_worldInverseMatrix" 
		-dt "matrix";
createNode network -n "rig_global_control_input_network";
	rename -uid "369D0120-4919-EBCD-52CD-918C6A59DE7B";
	addAttr -s false -ci true -sn "rig_global_control_input_network" -ln "rig_global_control_input_network" 
		-at "message";
	addAttr -ci true -sn "world_base_gd_0_worldMatrix" -ln "world_base_gd_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "world_base_gd_0_worldInverseMatrix" -ln "world_base_gd_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "world_01_gd_0_worldMatrix" -ln "world_01_gd_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "world_01_gd_0_worldInverseMatrix" -ln "world_01_gd_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "world_02_gd_0_worldMatrix" -ln "world_02_gd_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "world_02_gd_0_worldInverseMatrix" -ln "world_02_gd_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "cog_01_gd_0_worldMatrix" -ln "cog_01_gd_0_worldMatrix" -dt "matrix";
	addAttr -ci true -sn "cog_01_gd_0_worldInverseMatrix" -ln "cog_01_gd_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "setting_01_gd_0_worldMatrix" -ln "setting_01_gd_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "setting_01_gd_0_worldInverseMatrix" -ln "setting_01_gd_0_worldInverseMatrix" 
		-dt "matrix";
createNode network -n "rig_global_control_output_network";
	rename -uid "ABCA3397-465F-1403-6380-D888FA891F0F";
	addAttr -s false -ci true -sn "rig_global_control_output_network" -ln "rig_global_control_output_network" 
		-at "message";
	addAttr -ci true -sn "World_01_ctrl_0_worldMatrix" -ln "World_01_ctrl_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "World_01_ctrl_0_worldInverseMatrix" -ln "World_01_ctrl_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "World_02_ctrl_0_worldMatrix" -ln "World_02_ctrl_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "World_02_ctrl_0_worldInverseMatrix" -ln "World_02_ctrl_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "COG_ctrl_0_worldMatrix" -ln "COG_ctrl_0_worldMatrix" -dt "matrix";
	addAttr -ci true -sn "COG_ctrl_0_worldInverseMatrix" -ln "COG_ctrl_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "Setting_ctrl_0_worldMatrix" -ln "Setting_ctrl_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "Setting_ctrl_0_worldInverseMatrix" -ln "Setting_ctrl_0_worldInverseMatrix" 
		-dt "matrix";
createNode network -n "rig_global_skeleton_input_network";
	rename -uid "6276F568-471B-6342-B20E-2F80BFAA2663";
	addAttr -s false -ci true -sn "rig_global_skeleton_input_network" -ln "rig_global_skeleton_input_network" 
		-at "message";
	addAttr -ci true -sn "World_01_ctrl_0_worldMatrix" -ln "World_01_ctrl_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "World_01_ctrl_0_worldInverseMatrix" -ln "World_01_ctrl_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "World_02_ctrl_0_worldMatrix" -ln "World_02_ctrl_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "World_02_ctrl_0_worldInverseMatrix" -ln "World_02_ctrl_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "COG_ctrl_0_worldMatrix" -ln "COG_ctrl_0_worldMatrix" -dt "matrix";
	addAttr -ci true -sn "COG_ctrl_0_worldInverseMatrix" -ln "COG_ctrl_0_worldInverseMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "Setting_ctrl_0_worldMatrix" -ln "Setting_ctrl_0_worldMatrix" 
		-dt "matrix";
	addAttr -ci true -sn "Setting_ctrl_0_worldInverseMatrix" -ln "Setting_ctrl_0_worldInverseMatrix" 
		-dt "matrix";
createNode network -n "rig_global_skeleton_output_network";
	rename -uid "0067C747-4B12-AE56-9EC2-F1AE3339FD0B";
	addAttr -s false -ci true -sn "rig_global_skeleton_output_network" -ln "rig_global_skeleton_output_network" 
		-at "message";
createNode network -n "rig_global_misc_input_network";
	rename -uid "02886864-456D-08BE-0A91-1798BF545DC5";
	addAttr -s false -ci true -sn "rig_global_misc_input_network" -ln "rig_global_misc_input_network" 
		-at "message";
createNode network -n "rig_global_misc_output_network";
	rename -uid "ECC21CC8-4E89-254F-416E-9D8B126C4106";
	addAttr -s false -ci true -sn "rig_global_misc_output_network" -ln "rig_global_misc_output_network" 
		-at "message";
createNode bifrostBoard -n "ControlBase_bfGraph";
	rename -uid "B12687DE-45A8-012F-C4DC-7CAFACDBB60E";
	addAttr -w false -ci true -sn "world_base_gd_0" -ln "world_base_gd_0" -dt "bifData";
	addAttr -r false -ci true -k true -sn "JobPorts__Math_epsilonFloat" -ln "JobPorts__Math_epsilonFloat" 
		-at "float";
	addAttr -w false -ci true -sn "world_01_gd_0" -ln "world_01_gd_0" -dt "bifData";
	addAttr -w false -ci true -sn "world_02_gd_0" -ln "world_02_gd_0" -dt "bifData";
	addAttr -w false -ci true -sn "cog_01_gd_0" -ln "cog_01_gd_0" -dt "bifData";
	addAttr -w false -ci true -sn "setting_01_gd_0" -ln "setting_01_gd_0" -dt "bifData";
	addAttr -w false -ci true -sn "World_01_ctrl_0" -ln "World_01_ctrl_0" -dt "bifData";
	addAttr -w false -ci true -sn "World_02_ctrl_0" -ln "World_02_ctrl_0" -dt "bifData";
	addAttr -w false -ci true -sn "COG_ctrl_0" -ln "COG_ctrl_0" -dt "bifData";
	addAttr -w false -ci true -sn "Setting_ctrl_0" -ln "Setting_ctrl_0" -dt "bifData";
	setAttr ".sc" -type "string" (
		"{\n    \"header\": {\n        \"metadata\": [\n            {\n                \"metaName\": \"adskFileFormatVersion\",\n                \"metaValue\": \"100L\"\n            }\n        ]\n    },\n    \"dependencies\": [\n        {\n            \"uri\": \"file:///Math_types.json\"\n        },\n        {\n            \"uri\": \"file:///bifrost_object_i.json\"\n        },\n        {\n            \"uri\": \"file:///bifrost_geometry_query_types.json\"\n        },\n        {\n            \"uri\": \"file:///geometry_types.json\"\n        },\n        {\n            \"uri\": \"file:///validate_strands.json\"\n        },\n        {\n            \"uri\": \"file:///create_object_from_schema.json\"\n        },\n        {\n            \"uri\": \"file:///set_property_any.json\"\n        },\n        {\n            \"uri\": \"file:///set_property.json\"\n        },\n        {\n            \"uri\": \"file:///get_property_any.json\"\n        },\n        {\n            \"uri\": \"file:///get_property.json\"\n        },\n        {\n            \"uri\": \"file:///set_sub_object_property.json\"\n        },\n        {\n            \"uri\": \"file:///Math_conversion.json\"\n"
		+ "        },\n        {\n            \"uri\": \"file:///Math_float.json\"\n        },\n        {\n            \"uri\": \"file:///Math_double.json\"\n        },\n        {\n            \"uri\": \"file:///Math_long.json\"\n        },\n        {\n            \"uri\": \"file:///Math_char.json\"\n        },\n        {\n            \"uri\": \"file:///Math_int.json\"\n        },\n        {\n            \"uri\": \"file:///Math_short.json\"\n        },\n        {\n            \"uri\": \"file:///Math_uchar.json\"\n        },\n        {\n            \"uri\": \"file:///Math_uint.json\"\n        },\n        {\n            \"uri\": \"file:///Math_ulong.json\"\n        },\n        {\n            \"uri\": \"file:///Math_ushort.json\"\n        },\n        {\n            \"uri\": \"file:///riv_types.json\"\n        },\n        {\n            \"uri\": \"file:///point_types.json\"\n        },\n        {\n            \"uri\": \"file:///FCurve.json\"\n        },\n        {\n            \"uri\": \"file:///riv_ops.json\"\n        },\n        {\n            \"uri\": \"file:///Core_Array_array_is_empty.json\"\n        },\n        {\n            \"uri\": \"file:///CoreArrayOps.json\"\n"
		+ "        },\n        {\n            \"uri\": \"file:///get_geo_property.json\"\n        },\n        {\n            \"uri\": \"file:///has_property.json\"\n        },\n        {\n            \"uri\": \"file:///create_volume_geo_prop.json\"\n        },\n        {\n            \"uri\": \"file:///is_a.json\"\n        },\n        {\n            \"uri\": \"file:///is_a_mesh.json\"\n        },\n        {\n            \"uri\": \"file:///is_a_strands.json\"\n        },\n        {\n            \"uri\": \"file:///is_a_points.json\"\n        },\n        {\n            \"uri\": \"file:///is_a_volume.json\"\n        },\n        {\n            \"uri\": \"file:///get_geo_schema_type.json\"\n        },\n        {\n            \"uri\": \"file:///switch_is_a.json\"\n        },\n        {\n            \"uri\": \"file:///get_target_component.json\"\n        },\n        {\n            \"uri\": \"file:///create_data_geo_prop.json\"\n        },\n        {\n            \"uri\": \"file:///get_geo_component_count.json\"\n        },\n        {\n            \"uri\": \"file:///set_geo_property.array.json\"\n        },\n        {\n            \"uri\": \"file:///set_geo_property.scalar.json\"\n"
		+ "        },\n        {\n            \"uri\": \"file:///Math_multiply_quaternions.json\"\n        },\n        {\n            \"uri\": \"file:///Math_rotate_by_quaternion.json\"\n        },\n        {\n            \"uri\": \"file:///CoreStringOps.json\"\n        },\n        {\n            \"uri\": \"file:///Math_bool.json\"\n        },\n        {\n            \"uri\": \"file:///get_indexed_geo_property_check.json\"\n        },\n        {\n            \"uri\": \"file:///get_mesh_structure.json\"\n        },\n        {\n            \"uri\": \"file:///Math_array.json\"\n        },\n        {\n            \"uri\": \"file:///Core_Constants_default_value.json\"\n        },\n        {\n            \"uri\": \"file:///int_filter.json\"\n        },\n        {\n            \"uri\": \"file:///get_array_indices.json\"\n        },\n        {\n            \"uri\": \"file:///Math_matrix_to_quaternion.json\"\n        },\n        {\n            \"uri\": \"file:///erase_property.json\"\n        },\n        {\n            \"uri\": \"file:///Math_quaternion_to_matrix.json\"\n        },\n        {\n            \"uri\": \"file:///Math_compose_transform_matrix.json\"\n"
		+ "        },\n        {\n            \"uri\": \"file:///get_sub_object.json\"\n        },\n        {\n            \"uri\": \"file:///get_geo_property_or_default.json\"\n        },\n        {\n            \"uri\": \"file:///Math_quaternion_invert.json\"\n        },\n        {\n            \"uri\": \"file:///points_to_transforms.json\"\n        },\n        {\n            \"uri\": \"file:///get_geo_target_count.json\"\n        },\n        {\n            \"uri\": \"file:///get_geo_property_check.json\"\n        },\n        {\n            \"uri\": \"file:///volume_types.json\"\n        },\n        {\n            \"uri\": \"file:///volume_nodedefs.json\"\n        },\n        {\n            \"uri\": \"file:///interpret_auto_port_as_scalar.json\"\n        },\n        {\n            \"uri\": \"file:///Math_lerp_with_clamp.json\"\n        },\n        {\n            \"uri\": \"file:///Math_nlerp.json\"\n        },\n        {\n            \"uri\": \"file:///Math_quaternion_slerp.json\"\n        },\n        {\n            \"uri\": \"file:///transform_points.json\"\n        },\n        {\n            \"uri\": \"file:///Loc_Shape.json\"\n"
		+ "        },\n        {\n            \"uri\": \"file:///get_property_keys.json\"\n        },\n        {\n            \"uri\": \"file:///is_empty.json\"\n        },\n        {\n            \"uri\": \"file:///materials.json\"\n        },\n        {\n            \"uri\": \"file:///set_strands_shape.json\"\n        },\n        {\n            \"uri\": \"file:///construct_strands.json\"\n        },\n        {\n            \"uri\": \"file:///jotun_rand.json\"\n        },\n        {\n            \"uri\": \"file:///increment_decrement.json\"\n        },\n        {\n            \"uri\": \"file:///random_value.json\"\n        },\n        {\n            \"uri\": \"file:///access_offset_array.json\"\n        },\n        {\n            \"uri\": \"file:///get_strands_structure.json\"\n        },\n        {\n            \"uri\": \"file:///update_point_strand_index.json\"\n        },\n        {\n            \"uri\": \"file:///set_strand_color.json\"\n        },\n        {\n            \"uri\": \"file:///Global_shape.json\"\n        },\n        {\n            \"uri\": \"file:///fat_cross_shape.json\"\n        },\n        {\n            \"uri\": \"file:///COG_Shape.json\"\n"
		+ "        },\n        {\n            \"uri\": \"file:///setting_shape.json\"\n        }\n    ],\n    \"namespaces\": [],\n    \"types\": [],\n    \"compounds\": [\n        {\n            \"name\": \"ControlBase_bfGraph\",\n            \"metadata\": [\n                {\n                    \"metaName\": \"blackListed\",\n                    \"metaValue\": \"true\"\n                },\n                {\n                    \"metaName\": \"io_nodes\",\n                    \"metadata\": [\n                        {\n                            \"metaName\": \"io_inodes\",\n                            \"metadata\": [\n                                {\n                                    \"metaName\": \"input\"\n                                }\n                            ]\n                        },\n                        {\n                            \"metaName\": \"io_onodes\",\n                            \"metadata\": [\n                                {\n                                    \"metaName\": \"output\",\n                                    \"metadata\": [\n                                        {\n"
		+ "                                            \"metaName\": \"io_ports\",\n                                            \"metadata\": [\n                                                {\n                                                    \"metaName\": \"world_base_gd_0\"\n                                                },\n                                                {\n                                                    \"metaName\": \"world_01_gd_0\"\n                                                },\n                                                {\n                                                    \"metaName\": \"world_02_gd_0\"\n                                                },\n                                                {\n                                                    \"metaName\": \"cog_01_gd_0\"\n                                                },\n                                                {\n                                                    \"metaName\": \"setting_01_gd_0\"\n                                                },\n"
		+ "                                                {\n                                                    \"metaName\": \"World_01_ctrl_0\"\n                                                },\n                                                {\n                                                    \"metaName\": \"World_02_ctrl_0\"\n                                                },\n                                                {\n                                                    \"metaName\": \"COG_ctrl_0\"\n                                                },\n                                                {\n                                                    \"metaName\": \"Setting_ctrl_0\"\n                                                }\n                                            ]\n                                        }\n                                    ]\n                                }\n                            ]\n                        }\n                    ]\n                }\n            ],\n            \"ports\": [\n                {\n"
		+ "                    \"portName\": \"world_base_gd_0\",\n                    \"portDirection\": \"output\",\n                    \"portType\": \"Amino::Object\"\n                },\n                {\n                    \"portName\": \"world_01_gd_0\",\n                    \"portDirection\": \"output\",\n                    \"portType\": \"Amino::Object\"\n                },\n                {\n                    \"portName\": \"world_02_gd_0\",\n                    \"portDirection\": \"output\",\n                    \"portType\": \"Amino::Object\"\n                },\n                {\n                    \"portName\": \"cog_01_gd_0\",\n                    \"portDirection\": \"output\",\n                    \"portType\": \"Amino::Object\"\n                },\n                {\n                    \"portName\": \"setting_01_gd_0\",\n                    \"portDirection\": \"output\",\n                    \"portType\": \"Amino::Object\"\n                },\n                {\n                    \"portName\": \"World_01_ctrl_0\",\n                    \"portDirection\": \"output\",\n                    \"portType\": \"Amino::Object\"\n"
		+ "                },\n                {\n                    \"portName\": \"World_02_ctrl_0\",\n                    \"portDirection\": \"output\",\n                    \"portType\": \"Amino::Object\"\n                },\n                {\n                    \"portName\": \"COG_ctrl_0\",\n                    \"portDirection\": \"output\",\n                    \"portType\": \"Amino::Object\"\n                },\n                {\n                    \"portName\": \"Setting_ctrl_0\",\n                    \"portDirection\": \"output\",\n                    \"portType\": \"Amino::Object\"\n                }\n            ],\n            \"compoundNodes\": [\n                {\n                    \"nodeName\": \"Loc_Shape\",\n                    \"nodeType\": \"User::Compounds::Loc_Shape\"\n                },\n                {\n                    \"nodeName\": \"Loc_Shape1\",\n                    \"nodeType\": \"User::Compounds::Loc_Shape\"\n                },\n                {\n                    \"nodeName\": \"Loc_Shape2\",\n                    \"nodeType\": \"User::Compounds::Loc_Shape\"\n                },\n"
		+ "                {\n                    \"nodeName\": \"Loc_Shape3\",\n                    \"nodeType\": \"User::Compounds::Loc_Shape\"\n                },\n                {\n                    \"nodeName\": \"Loc_Shape4\",\n                    \"nodeType\": \"User::Compounds::Loc_Shape\"\n                },\n                {\n                    \"nodeName\": \"Global_shape\",\n                    \"nodeType\": \"User::Compounds::Global_shape\"\n                },\n                {\n                    \"nodeName\": \"fat_cross_shape\",\n                    \"nodeType\": \"User::Compounds::fat_cross_shape\"\n                },\n                {\n                    \"nodeName\": \"COG_Shape\",\n                    \"nodeType\": \"User::Compounds::COG_Shape\"\n                },\n                {\n                    \"nodeName\": \"setting_shape\",\n                    \"nodeType\": \"User::Compounds::setting_shape\"\n                }\n            ],\n            \"connections\": [\n                {\n                    \"source\": \"Loc_Shape.Loc_Shape\",\n                    \"target\": \".world_base_gd_0\"\n"
		+ "                },\n                {\n                    \"source\": \"Loc_Shape1.Loc_Shape\",\n                    \"target\": \".world_01_gd_0\"\n                },\n                {\n                    \"source\": \"Loc_Shape2.Loc_Shape\",\n                    \"target\": \".world_02_gd_0\"\n                },\n                {\n                    \"source\": \"Loc_Shape3.Loc_Shape\",\n                    \"target\": \".cog_01_gd_0\"\n                },\n                {\n                    \"source\": \"Loc_Shape4.Loc_Shape\",\n                    \"target\": \".setting_01_gd_0\"\n                },\n                {\n                    \"source\": \"Global_shape.Global_shape\",\n                    \"target\": \".World_01_ctrl_0\"\n                },\n                {\n                    \"source\": \"fat_cross_shape.fat_cross_shape\",\n                    \"target\": \".World_02_ctrl_0\"\n                },\n                {\n                    \"source\": \"COG_Shape.COG_Shape\",\n                    \"target\": \".COG_ctrl_0\"\n                },\n                {\n                    \"source\": \"setting_shape.setting_shape\",\n"
		+ "                    \"target\": \".Setting_ctrl_0\"\n                }\n            ],\n            \"values\": [\n                {\n                    \"valueName\": \"Global_shape.offset\",\n                    \"valueType\": \"Math::float4x4\",\n                    \"value\": {\n                        \"c0\": {\n                            \"x\": \"1f\",\n                            \"y\": \"0f\",\n                            \"z\": \"0f\",\n                            \"w\": \"0f\"\n                        },\n                        \"c1\": {\n                            \"x\": \"0f\",\n                            \"y\": \"1f\",\n                            \"z\": \"0f\",\n                            \"w\": \"0f\"\n                        },\n                        \"c2\": {\n                            \"x\": \"0f\",\n                            \"y\": \"0f\",\n                            \"z\": \"1f\",\n                            \"w\": \"0f\"\n                        },\n                        \"c3\": {\n                            \"x\": \"0f\",\n                            \"y\": \"0f\",\n                            \"z\": \"0f\",\n"
		+ "                            \"w\": \"1f\"\n                        }\n                    }\n                },\n                {\n                    \"valueName\": \"Global_shape.colormin\",\n                    \"valueType\": \"Math::float3\",\n                    \"value\": {\n                        \"x\": \"10f\",\n                        \"y\": \"10f\",\n                        \"z\": \"0f\"\n                    }\n                },\n                {\n                    \"valueName\": \"Global_shape.colormax\",\n                    \"valueType\": \"Math::float3\",\n                    \"value\": {\n                        \"x\": \"10f\",\n                        \"y\": \"10f\",\n                        \"z\": \"0f\"\n                    }\n                },\n                {\n                    \"valueName\": \"Global_shape.default_size\",\n                    \"valueType\": \"float\",\n                    \"value\": \"0.0500000007f\"\n                },\n                {\n                    \"valueName\": \"fat_cross_shape.offset\",\n                    \"valueType\": \"Math::float4x4\",\n"
		+ "                    \"value\": {\n                        \"c0\": {\n                            \"x\": \"0.699999988f\",\n                            \"y\": \"0f\",\n                            \"z\": \"0f\",\n                            \"w\": \"0f\"\n                        },\n                        \"c1\": {\n                            \"x\": \"0f\",\n                            \"y\": \"0.699999988f\",\n                            \"z\": \"0f\",\n                            \"w\": \"0f\"\n                        },\n                        \"c2\": {\n                            \"x\": \"0f\",\n                            \"y\": \"0f\",\n                            \"z\": \"0.699999988f\",\n                            \"w\": \"0f\"\n                        },\n                        \"c3\": {\n                            \"x\": \"0f\",\n                            \"y\": \"0f\",\n                            \"z\": \"0f\",\n                            \"w\": \"1f\"\n                        }\n                    }\n                },\n                {\n                    \"valueName\": \"fat_cross_shape.colormin\",\n"
		+ "                    \"valueType\": \"Math::float3\",\n                    \"value\": {\n                        \"x\": \"0f\",\n                        \"y\": \"12f\",\n                        \"z\": \"12f\"\n                    }\n                },\n                {\n                    \"valueName\": \"fat_cross_shape.colormax\",\n                    \"valueType\": \"Math::float3\",\n                    \"value\": {\n                        \"x\": \"0f\",\n                        \"y\": \"12f\",\n                        \"z\": \"12f\"\n                    }\n                },\n                {\n                    \"valueName\": \"fat_cross_shape.default_size\",\n                    \"valueType\": \"float\",\n                    \"value\": \"0.0299999993f\"\n                },\n                {\n                    \"valueName\": \"COG_Shape.colormax\",\n                    \"valueType\": \"Math::float3\",\n                    \"value\": {\n                        \"x\": \"10f\",\n                        \"y\": \"10f\",\n                        \"z\": \"0f\"\n                    }\n                },\n                {\n"
		+ "                    \"valueName\": \"COG_Shape.default_size\",\n                    \"valueType\": \"float\",\n                    \"value\": \"0.0299999993f\"\n                },\n                {\n                    \"valueName\": \"setting_shape.offset\",\n                    \"valueType\": \"Math::float4x4\",\n                    \"value\": {\n                        \"c0\": {\n                            \"x\": \"0.5f\",\n                            \"y\": \"0f\",\n                            \"z\": \"0f\",\n                            \"w\": \"0f\"\n                        },\n                        \"c1\": {\n                            \"x\": \"0f\",\n                            \"y\": \"0.5f\",\n                            \"z\": \"0f\",\n                            \"w\": \"0f\"\n                        },\n                        \"c2\": {\n                            \"x\": \"0f\",\n                            \"y\": \"0f\",\n                            \"z\": \"0.5f\",\n                            \"w\": \"0f\"\n                        },\n                        \"c3\": {\n                            \"x\": \"0f\",\n"
		+ "                            \"y\": \"0f\",\n                            \"z\": \"0f\",\n                            \"w\": \"1f\"\n                        }\n                    }\n                },\n                {\n                    \"valueName\": \"setting_shape.colormin\",\n                    \"valueType\": \"Math::float3\",\n                    \"value\": {\n                        \"x\": \"0f\",\n                        \"y\": \"12f\",\n                        \"z\": \"12f\"\n                    }\n                },\n                {\n                    \"valueName\": \"setting_shape.colormax\",\n                    \"valueType\": \"Math::float3\",\n                    \"value\": {\n                        \"x\": \"0f\",\n                        \"y\": \"12f\",\n                        \"z\": \"12f\"\n                    }\n                },\n                {\n                    \"valueName\": \"setting_shape.default_size\",\n                    \"valueType\": \"float\",\n                    \"value\": \"0.0299999993f\"\n                }\n            ],\n            \"reservedNodeNames\": [\n"
		+ "                {\n                    \"name\": \"input\"\n                },\n                {\n                    \"name\": \"output\"\n                }\n            ]\n        }\n    ]\n}\n");
	setAttr ".dirtyFlag" yes;
createNode multMatrix -n "world_01_to_world_02";
	rename -uid "A0829255-466B-CBAB-07D9-83B3AC7C83CE";
	setAttr -s 3 ".i";
createNode multMatrix -n "world_02_to_COG";
	rename -uid "64C2B0D6-41CB-C36D-F4B3-7C8D3762D5E8";
	setAttr -s 3 ".i";
createNode multMatrix -n "COG_to_setting";
	rename -uid "C2580344-4812-BA06-3810-6B80E1C5C17A";
	setAttr -s 3 ".i";
createNode script -n "uiConfigurationScriptNode";
	rename -uid "D7065524-4C2C-826E-4519-C2AF681B14ED";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1362\n            -height 725\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n"
		+ "            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"print(\\\"\\\")\" \n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n"
		+ "            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n"
		+ "            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"0\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n"
		+ "            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n"
		+ "                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n"
		+ "                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n"
		+ "                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -keyMinScale 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 1\n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n"
		+ "                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n"
		+ "                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n"
		+ "                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n"
		+ "            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n"
		+ "                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n"
		+ "                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n"
		+ "                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1362\\n    -height 725\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1362\\n    -height 725\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "FEE3F8C1-45A2-F396-7148-3EBD67E499DA";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -s 9 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".ren" -type "string" "arnold";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio";
	setAttr ".wsn" -type "string" "ACEScg";
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "rig_global_input_network.rig_global_input_network" "rig_global.rig_global_input_network"
		;
connectAttr "rig_global_guide_input_network.rig_global_guide_input_network" "rig_global_guides.rig_global_guide_input_network"
		;
connectAttr "ControlBase_bfGraph.world_base_gd_0" "world_base_gd_Shape0.is";
connectAttr "world_base_gd_0.wm" "world_01_gd_0.opm";
connectAttr "ControlBase_bfGraph.world_01_gd_0" "world_01_gd_Shape0.is";
connectAttr "world_01_gd_0.wm" "world_02_gd_0.opm";
connectAttr "ControlBase_bfGraph.world_02_gd_0" "world_02_gd_Shape0.is";
connectAttr "world_02_gd_0.wm" "cog_01_gd_0.opm";
connectAttr "ControlBase_bfGraph.cog_01_gd_0" "cog_01_gd_Shape0.is";
connectAttr "cog_01_gd_0.wm" "setting_01_gd_0.opm";
connectAttr "ControlBase_bfGraph.setting_01_gd_0" "setting_01_gd_Shape0.is";
connectAttr "rig_global_control_input_network.rig_global_control_input_network" "rig_global_controls.rig_global_control_input_network"
		;
connectAttr "rig_global_control_input_network.world_01_gd_0_worldMatrix" "World_01_ctrl_0.opm"
		;
connectAttr "ControlBase_bfGraph.World_01_ctrl_0" "World_01_ctrl_Shape0.is";
connectAttr "world_01_to_world_02.o" "World_02_ctrl_0.opm";
connectAttr "ControlBase_bfGraph.World_02_ctrl_0" "World_02_ctrl_Shape0.is";
connectAttr "world_02_to_COG.o" "COG_ctrl_0.opm";
connectAttr "ControlBase_bfGraph.COG_ctrl_0" "COG_ctrl_Shape0.is";
connectAttr "COG_to_setting.o" "Setting_ctrl_0.opm";
connectAttr "ControlBase_bfGraph.Setting_ctrl_0" "Setting_ctrl_Shape0.is";
connectAttr "rig_global_skeleton_input_network.rig_global_skeleton_input_network" "rig_global_skeleton.rig_global_skeleton_input_network"
		;
connectAttr "rig_global_skeleton_input_network.World_01_ctrl_0_worldMatrix" "World_01_ctrl_0_jnt.opm"
		;
connectAttr "World_01_ctrl_0_jnt.s" "World_02_ctrl_0_jnt.is";
connectAttr "rig_global_skeleton_input_network.World_02_ctrl_0_worldMatrix" "World_02_ctrl_0_jnt.opm"
		;
connectAttr "World_02_ctrl_0_jnt.s" "COG_ctrl_0_jnt.is";
connectAttr "rig_global_skeleton_input_network.COG_ctrl_0_worldMatrix" "COG_ctrl_0_jnt.opm"
		;
connectAttr "COG_ctrl_0_jnt.s" "Setting_ctrl_0_jnt.is";
connectAttr "rig_global_skeleton_input_network.Setting_ctrl_0_worldMatrix" "Setting_ctrl_0_jnt.opm"
		;
connectAttr "rig_global_misc_input_network.rig_global_misc_input_network" "rig_global_misc.rig_global_misc_input_network"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "rig_global.rig_global_output_network" "rig_global_output_network.rig_global_output_network"
		;
connectAttr "rig_global_guides.rig_global_guide_output_network" "rig_global_guide_output_network.rig_global_guide_output_network"
		;
connectAttr "world_base_gd_0.wm" "rig_global_guide_output_network.world_base_gd_0_worldMatrix"
		;
connectAttr "world_base_gd_0.wim" "rig_global_guide_output_network.world_base_gd_0_worldInverseMatrix"
		;
connectAttr "world_01_gd_0.wm" "rig_global_guide_output_network.world_01_gd_0_worldMatrix"
		;
connectAttr "world_01_gd_0.wim" "rig_global_guide_output_network.world_01_gd_0_worldInverseMatrix"
		;
connectAttr "world_02_gd_0.wm" "rig_global_guide_output_network.world_02_gd_0_worldMatrix"
		;
connectAttr "world_02_gd_0.wim" "rig_global_guide_output_network.world_02_gd_0_worldInverseMatrix"
		;
connectAttr "cog_01_gd_0.wm" "rig_global_guide_output_network.cog_01_gd_0_worldMatrix"
		;
connectAttr "cog_01_gd_0.wim" "rig_global_guide_output_network.cog_01_gd_0_worldInverseMatrix"
		;
connectAttr "setting_01_gd_0.wm" "rig_global_guide_output_network.setting_01_gd_0_worldMatrix"
		;
connectAttr "setting_01_gd_0.wim" "rig_global_guide_output_network.setting_01_gd_0_worldInverseMatrix"
		;
connectAttr "rig_global_guide_output_network.world_base_gd_0_worldMatrix" "rig_global_control_input_network.world_base_gd_0_worldMatrix"
		;
connectAttr "rig_global_guide_output_network.world_base_gd_0_worldInverseMatrix" "rig_global_control_input_network.world_base_gd_0_worldInverseMatrix"
		;
connectAttr "rig_global_guide_output_network.world_01_gd_0_worldMatrix" "rig_global_control_input_network.world_01_gd_0_worldMatrix"
		;
connectAttr "rig_global_guide_output_network.world_01_gd_0_worldInverseMatrix" "rig_global_control_input_network.world_01_gd_0_worldInverseMatrix"
		;
connectAttr "rig_global_guide_output_network.world_02_gd_0_worldMatrix" "rig_global_control_input_network.world_02_gd_0_worldMatrix"
		;
connectAttr "rig_global_guide_output_network.world_02_gd_0_worldInverseMatrix" "rig_global_control_input_network.world_02_gd_0_worldInverseMatrix"
		;
connectAttr "rig_global_guide_output_network.cog_01_gd_0_worldMatrix" "rig_global_control_input_network.cog_01_gd_0_worldMatrix"
		;
connectAttr "rig_global_guide_output_network.cog_01_gd_0_worldInverseMatrix" "rig_global_control_input_network.cog_01_gd_0_worldInverseMatrix"
		;
connectAttr "rig_global_guide_output_network.setting_01_gd_0_worldMatrix" "rig_global_control_input_network.setting_01_gd_0_worldMatrix"
		;
connectAttr "rig_global_guide_output_network.setting_01_gd_0_worldInverseMatrix" "rig_global_control_input_network.setting_01_gd_0_worldInverseMatrix"
		;
connectAttr "rig_global_controls.rig_global_control_output_network" "rig_global_control_output_network.rig_global_control_output_network"
		;
connectAttr "World_01_ctrl_0.wm" "rig_global_control_output_network.World_01_ctrl_0_worldMatrix"
		;
connectAttr "World_01_ctrl_0.wim" "rig_global_control_output_network.World_01_ctrl_0_worldInverseMatrix"
		;
connectAttr "World_02_ctrl_0.wm" "rig_global_control_output_network.World_02_ctrl_0_worldMatrix"
		;
connectAttr "World_02_ctrl_0.wim" "rig_global_control_output_network.World_02_ctrl_0_worldInverseMatrix"
		;
connectAttr "COG_ctrl_0.wm" "rig_global_control_output_network.COG_ctrl_0_worldMatrix"
		;
connectAttr "COG_ctrl_0.wim" "rig_global_control_output_network.COG_ctrl_0_worldInverseMatrix"
		;
connectAttr "Setting_ctrl_0.wm" "rig_global_control_output_network.Setting_ctrl_0_worldMatrix"
		;
connectAttr "Setting_ctrl_0.wim" "rig_global_control_output_network.Setting_ctrl_0_worldInverseMatrix"
		;
connectAttr "rig_global_control_output_network.World_01_ctrl_0_worldMatrix" "rig_global_skeleton_input_network.World_01_ctrl_0_worldMatrix"
		;
connectAttr "rig_global_control_output_network.World_01_ctrl_0_worldInverseMatrix" "rig_global_skeleton_input_network.World_01_ctrl_0_worldInverseMatrix"
		;
connectAttr "rig_global_control_output_network.World_02_ctrl_0_worldMatrix" "rig_global_skeleton_input_network.World_02_ctrl_0_worldMatrix"
		;
connectAttr "rig_global_control_output_network.World_02_ctrl_0_worldInverseMatrix" "rig_global_skeleton_input_network.World_02_ctrl_0_worldInverseMatrix"
		;
connectAttr "rig_global_control_output_network.COG_ctrl_0_worldMatrix" "rig_global_skeleton_input_network.COG_ctrl_0_worldMatrix"
		;
connectAttr "rig_global_control_output_network.COG_ctrl_0_worldInverseMatrix" "rig_global_skeleton_input_network.COG_ctrl_0_worldInverseMatrix"
		;
connectAttr "rig_global_control_output_network.Setting_ctrl_0_worldMatrix" "rig_global_skeleton_input_network.Setting_ctrl_0_worldMatrix"
		;
connectAttr "rig_global_control_output_network.Setting_ctrl_0_worldInverseMatrix" "rig_global_skeleton_input_network.Setting_ctrl_0_worldInverseMatrix"
		;
connectAttr "rig_global_skeleton.rig_global_skeleton_output_network" "rig_global_skeleton_output_network.rig_global_skeleton_output_network"
		;
connectAttr "rig_global_misc.rig_global_misc_output_network" "rig_global_misc_output_network.rig_global_misc_output_network"
		;
connectAttr "rig_global_control_input_network.world_02_gd_0_worldMatrix" "world_01_to_world_02.i[0]"
		;
connectAttr "rig_global_control_input_network.world_01_gd_0_worldInverseMatrix" "world_01_to_world_02.i[1]"
		;
connectAttr "World_01_ctrl_0.wm" "world_01_to_world_02.i[2]";
connectAttr "rig_global_control_input_network.cog_01_gd_0_worldMatrix" "world_02_to_COG.i[0]"
		;
connectAttr "rig_global_control_input_network.world_02_gd_0_worldInverseMatrix" "world_02_to_COG.i[1]"
		;
connectAttr "World_02_ctrl_0.wm" "world_02_to_COG.i[2]";
connectAttr "rig_global_control_input_network.setting_01_gd_0_worldMatrix" "COG_to_setting.i[0]"
		;
connectAttr "rig_global_control_input_network.cog_01_gd_0_worldInverseMatrix" "COG_to_setting.i[1]"
		;
connectAttr "COG_ctrl_0.wm" "COG_to_setting.i[2]";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "world_base_gd_Shape0.iog" ":initialShadingGroup.dsm" -na;
connectAttr "world_01_gd_Shape0.iog" ":initialShadingGroup.dsm" -na;
connectAttr "world_02_gd_Shape0.iog" ":initialShadingGroup.dsm" -na;
connectAttr "cog_01_gd_Shape0.iog" ":initialShadingGroup.dsm" -na;
connectAttr "setting_01_gd_Shape0.iog" ":initialShadingGroup.dsm" -na;
connectAttr "World_01_ctrl_Shape0.iog" ":initialShadingGroup.dsm" -na;
connectAttr "World_02_ctrl_Shape0.iog" ":initialShadingGroup.dsm" -na;
connectAttr "COG_ctrl_Shape0.iog" ":initialShadingGroup.dsm" -na;
connectAttr "Setting_ctrl_Shape0.iog" ":initialShadingGroup.dsm" -na;
// End of Script.ma
