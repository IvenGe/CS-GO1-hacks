from time import sleep

import pymem as pymem
import threading

import win32api
import win32con

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
print("CS:GO has process id: " + str(pm.process_id))
print('Cheat has been initialized.')

# offsets




# 2022-05-16 13:58:09.442745700 UTC


timestamp = 1652709489

cs_gamerules_data = 0x0
m_ArmorValue = 0x117CC
m_Collision = 0x320
m_CollisionGroup = 0x474
m_Local = 0x2FCC
m_MoveType = 0x25C
m_OriginalOwnerXuidHigh = 0x31D4
m_OriginalOwnerXuidLow = 0x31D0
m_SurvivalGameRuleDecisionTypes = 0x1328
m_SurvivalRules = 0xD00
m_aimPunchAngle = 0x303C
m_aimPunchAngleVel = 0x3048
m_angEyeAnglesX = 0x117D0
m_angEyeAnglesY = 0x117D4
m_bBombDefused = 0x29C0
m_bBombPlanted = 0x9A5
m_bBombTicking = 0x2990
m_bFreezePeriod = 0x20
m_bGunGameImmunity = 0x9990
m_bHasDefuser = 0x117DC
m_bHasHelmet = 0x117C0
m_bInReload = 0x32B5
m_bIsDefusing = 0x997C
m_bIsQueuedMatchmaking = 0x74
m_bIsScoped = 0x9974
m_bIsValveDS = 0x7C
m_bSpotted = 0x93D
m_bSpottedByMask = 0x980
m_bStartedArming = 0x3400
m_bUseCustomAutoExposureMax = 0x9D9
m_bUseCustomAutoExposureMin = 0x9D8
m_bUseCustomBloomScale = 0x9DA
m_clrRender = 0x70
m_dwBoneMatrix = 0x26A8
m_fAccuracyPenalty = 0x3340
m_fFlags = 0x104
m_flC4Blow = 0x29A0
m_flCustomAutoExposureMax = 0x9E0
m_flCustomAutoExposureMin = 0x9DC
m_flCustomBloomScale = 0x9E4
m_flDefuseCountDown = 0x29BC
m_flDefuseLength = 0x29B8
m_flFallbackWear = 0x31E0
m_flFlashDuration = 0x10470
m_flFlashMaxAlpha = 0x1046C
m_flLastBoneSetupTime = 0x2928
m_flLowerBodyYawTarget = 0x9ADC
m_flNextAttack = 0x2D80
m_flNextPrimaryAttack = 0x3248
m_flSimulationTime = 0x268
m_flTimerLength = 0x29A4
m_hActiveWeapon = 0x2F08
m_hBombDefuser = 0x29C4
m_hMyWeapons = 0x2E08
m_hObserverTarget = 0x339C
m_hOwner = 0x29DC
m_hOwnerEntity = 0x14C
m_hViewModel = 0x3308
m_iAccountID = 0x2FD8
m_iClip1 = 0x3274
m_iCompetitiveRanking = 0x1A84
m_iCompetitiveWins = 0x1B88
m_iCrosshairId = 0x11838
m_iDefaultFOV = 0x333C
m_iEntityQuality = 0x2FBC
m_iFOV = 0x31F4
m_iFOVStart = 0x31F8
m_iGlowIndex = 0x10488
m_iHealth = 0x100
m_iItemDefinitionIndex = 0x2FBA
m_iItemIDHigh = 0x2FD0
m_iMostRecentModelBoneCounter = 0x2690
m_iObserverMode = 0x3388
m_iShotsFired = 0x103E0
m_iState = 0x3268
m_iTeamNum = 0xF4
m_lifeState = 0x25F
m_nBombSite = 0x2994
m_nFallbackPaintKit = 0x31D8
m_nFallbackSeed = 0x31DC
m_nFallbackStatTrak = 0x31E4
m_nForceBone = 0x268C
m_nTickBase = 0x3440
m_nViewModelIndex = 0x29D0
m_rgflCoordinateFrame = 0x444
m_szCustomName = 0x304C
m_szLastPlaceName = 0x35C4
m_thirdPersonViewAngles = 0x31E8
m_vecOrigin = 0x138
m_vecVelocity = 0x114
m_vecViewOffset = 0x108
m_viewPunchAngle = 0x3030
m_zoomLevel = 0x33E0

anim_overlays = 0x2990
clientstate_choked_commands = 0x4D30
clientstate_delta_ticks = 0x174
clientstate_last_outgoing_command = 0x4D2C
clientstate_net_channel = 0x9C
convar_name_hash_table = 0x2F0F8
dwClientState = 0x58CFBC
dwClientState_GetLocalPlayer = 0x180
dwClientState_IsHLTV = 0x4D48
dwClientState_Map = 0x28C
dwClientState_MapDirectory = 0x188
dwClientState_MaxPlayer = 0x388
dwClientState_PlayerInfo = 0x52C0
dwClientState_State = 0x108
dwClientState_ViewAngles = 0x4D90
dwEntityList = 0x4DD344C
dwForceAttack = 0x32038F4
dwForceAttack2 = 0x3203900
dwForceBackward = 0x3203924
dwForceForward = 0x3203918
dwForceJump = 0x527D360
dwForceLeft = 0x3203930
dwForceRight = 0x320393C
dwGameDir = 0x62B900
dwGameRulesProxy = 0x52F0B8C
dwGetAllClasses = 0xDE177C
dwGlobalVars = 0x58CCC0
dwGlowObjectManager = 0x531C058
dwInput = 0x5224A20
dwInterfaceLinkList = 0x9698B4
dwLocalPlayer = 0xDB75DC
dwMouseEnable = 0xDBD2E8
dwMouseEnablePtr = 0xDBD2B8
dwPlayerResource = 0x3201CB0
dwRadarBase = 0x52081C4
dwSensitivity = 0xDBD184
dwSensitivityPtr = 0xDBD158
dwSetClanTag = 0x8A3A0
dwViewMatrix = 0x4DC4D64
dwWeaponTable = 0x52254E4
dwWeaponTableIndex = 0x326C
dwYawPtr = 0xDBCF48
dwZoomSensitivityRatioPtr = 0xDC31B0
dwbSendPackets = 0xD96A2
dwppDirect3DDevice9 = 0xA5050
find_hud_element = 0x2D655200
force_update_spectator_glow = 0x3BB99A
interface_engine_cvar = 0x3E9EC
is_c4_owner = 0x3C8A10
m_bDormant = 0xED
m_flSpawnTime = 0x103C0
m_pStudioHdr = 0x2950
m_pitchClassPtr = 0x5208460
m_yawClassPtr = 0xDBCF48
model_ambient_min = 0x590034
set_abs_angles = 0x1E5570
set_abs_origin = 0x1E53B0





# getters
def get_player(index):
    return pm.read_int(client + dwEntityList + index * 0x10)  # every player is a int


def get_local_player():
    return pm.read_int(client + dwLocalPlayer)


def get_cross_hair_id(player_id):
    return pm.read_int(player_id + m_iCrosshairId)


def get_team(player_id):
    return pm.read_int(player_id + m_iTeamNum)


def get_name_by_id(idd):
    idd = int(idd)
    radar_base = pm.read_int(client + dwRadarBase)
    c_hud_radar = pm.read_int(radar_base + 0x74)

    # print(pm.read_string(c_hud_radar + 0x300 + (0x174 * (id - 1))))
    return pm.read_string(c_hud_radar + 0x300 + (0x174 * (idd - 1)))


# Hacks
def radar():
    while True:
        for i in range(1, 32):
            entity = get_player(i)
            if entity:
                pm.write_bool(entity + m_bSpotted, True)
                sleep(0.02)


def trigger_bot():
    while True:
        cross_hair_id = get_cross_hair_id(get_local_player())
        cross_hair_Team = get_team(get_player(cross_hair_id - 1))
        local_team = get_team(get_local_player())

        if 0 < cross_hair_id < 32 and local_team != cross_hair_Team and win32api.GetAsyncKeyState(
                win32con.VK_MENU) == -32767:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            sleep(0.25)
        sleep(0.10)  # makes it more legit the lower how more accurate


ranks = ["Unranked", "Silver I", "Silver II", "Silver III", "Silver IV", "Silver Elite", "Silver Elite Master",
         "Gold Nova I", "Gold Nova II", "Gold Nova III", "Gold Nova Elite", "Master Guardian I", "Master Guardian II",
         "Master Guardian Elite", "Distinguished Master Guardian", "Legendary Eagle", "Legendary Eagle Master",
         "Supreme Master First Class", "The Global Elite"]


def reveal_ranks():
    for i in range(1, 32):
        entity = get_player(i)
        if entity > 0:
            player_resource = pm.read_int(client + dwPlayerResource)

            rank = pm.read_int(player_resource + m_iCompetitiveRanking + i * 4)
            wins = pm.read_int(player_resource + m_iCompetitiveWins + i * 4)
            health = pm.read_int(player_resource + m_iHealth + i * 4)
            # print(get_name_by_id(i).encode(encoding='utf-8', errors='ignore').strip())
            try:
                print("id: " + str(i) + " " + get_name_by_id(i) + " is " + ranks[rank] + " and has " + str(
                    wins) + " wins and is HP:" + str(health))
            except:
                print('')


def b_hop():
    while True:
        flags = pm.read_int(get_local_player() + m_fFlags)

        if flags == 257 and win32api.GetAsyncKeyState(
                win32con.VK_SPACE) < -32000:
            pm.write_int(client + dwForceJump, 5)
            sleep(0.45)
            pm.write_int(client + dwForceJump, 4)


# Threads
walls = threading.Thread(target=radar)
walls.start()
trigger = threading.Thread(target=trigger_bot)
trigger.start()
b_hop = threading.Thread(target=b_hop)
b_hop.start()

reveal_ranks()
