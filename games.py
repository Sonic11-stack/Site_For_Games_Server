from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/the_last_of_us")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("The Last Of Us.html", {"request": request})

@router.get("/the_last_of_us_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("The_Last_of_Us_2.html", {"request": request})

@router.get("/horizon_zero_dawn")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Horizon_Zero_Dawn.html", {"request": request})

@router.get("/horizon_forbidden_west")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Horizon_Forbidden_West.html", {"request": request})

@router.get("/mass_effect")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mass_Effect.html", {"request": request})

@router.get("/mass_effect_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mass_Effect_2.html", {"request": request})

@router.get("/mass_effect_3")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mass_Effect_3.html", {"request": request})

@router.get("/mortal_kombat_9")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mortal_Kombat_9.html", {"request": request})

@router.get("/mortal_kombat_10")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mortal_Kombat_10.html", {"request": request})

@router.get("/mortal_kombat_11")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mortal_Kombat_11.html", {"request": request})

@router.get("/mortal_kombat_1")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mortal_Kombat_1.html", {"request": request})

@router.get("/portal")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Portal.html", {"request": request})

@router.get("/portal_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Portal_2.html", {"request": request})

@router.get("/wow")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("WOW.html", {"request": request})

@router.get("/cyberpunk")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Cyberpunk.html", {"request": request})

@router.get("/gta5")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("GTA5.html", {"request": request})

@router.get("/minecraft")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Minecraft.html", {"request": request})

@router.get("/half_life")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Half_Life.html", {"request": request})

@router.get("/half_life_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Half_Life_2.html", {"request": request})

@router.get("/witcher_3")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Witcher_3.html", {"request": request})

@router.get("/tomb_raider")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Tomb_Raider.html", {"request": request})

@router.get("/spore")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Spore.html", {"request": request})

@router.get("/team_fortress_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Team_Fortress_2.html", {"request": request})

@router.get("/terraria")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Terraria.html", {"request": request})

@router.get("/dark_souls")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Dark_Souls.html", {"request": request})

@router.get("/dark_souls_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Dark_Souls_2.html", {"request": request})

@router.get("/dark_souls_3")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Dark_Souls_3.html", {"request": request})

@router.get("/elden_ring")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Elden_Ring.html", {"request": request})

@router.get("/walking_dead")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Walking_Dead.html", {"request": request})

@router.get("/sims_4")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Sims_4.html", {"request": request})

@router.get("/doom")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Doom_Eternal.html", {"request": request})

@router.get("/mgr")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("MGR.html", {"request": request})

@router.get("/death_stranding")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Death_Stranding.html", {"request": request})

@router.get("/garry's_mod")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Garry's_Mod.html", {"request": request})

@router.get("/don't_starve")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Don't_Starve.html", {"request": request})

@router.get("/hearthstone")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Hearthstone.html", {"request": request})

@router.get("/mtg")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("MTG.html", {"request": request})

@router.get("/detroit")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Detroit.html", {"request": request})

@router.get("/need_for_speed")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Need_For_Speed.html", {"request": request})

@router.get("/pubg")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("PUBG.html", {"request": request})

@router.get("/apex")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Apex_Legends.html", {"request": request})

@router.get("/fortnite")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Fortnite.html", {"request": request})

@router.get("/isaac")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Isaac.html", {"request": request})

@router.get("/undertale")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Undertale.html", {"request": request})

@router.get("/sackboy")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Sackboy.html", {"request": request})

@router.get("/hollow_night")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Hollow_Night.html", {"request": request})

@router.get("/freddy")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Freddy.html", {"request": request}) 

@router.get("/wolfenstein")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Wolfenstein.html", {"request": request}) 

@router.get("/wolfenstein_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Wolfenstein_2.html", {"request": request}) 

@router.get("/silent_hill")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Silent_Hill.html", {"request": request}) 

@router.get("/silent_hill_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Silent_Hill_2.html", {"request": request}) 

@router.get("/middle_earth")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Middle_Earth.html", {"request": request}) 

@router.get("/middle_earth_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Middle_Earth_2.html", {"request": request}) 

@router.get("/for_honor")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("For_Honor.html", {"request": request}) 

@router.get("/tsushima")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Tsushima.html", {"request": request}) 

@router.get("/way_out")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Way_out.html", {"request": request}) 

@router.get("/until_dawn")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Until_Dawn.html", {"request": request}) 

@router.get("/quarry")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Quarry.html", {"request": request}) 

@router.get("/rust")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Rust.html", {"request": request}) 

@router.get("/nier")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Nier.html", {"request": request}) 

@router.get("/metro")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Metro.html", {"request": request}) 

@router.get("/metro_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Metro_2.html", {"request": request}) 

@router.get("/metro_3")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Metro_3.html", {"request": request}) 

@router.get("/cuphead")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Cuphead.html", {"request": request}) 

@router.get("/little_nightmares")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Little_Nightmares.html", {"request": request}) 

@router.get("/little_nightmares_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Little_Nightmares_2.html", {"request": request}) 

@router.get("/subnautica")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Subnautica.html", {"request": request}) 

@router.get("/subnautica_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Subnautica_2.html", {"request": request}) 

@router.get("/stardew_valley")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Stardew_Valley.html", {"request": request}) 

@router.get("/baldur's_gate_3")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Baldur's_Gate_3.html", {"request": request}) 

@router.get("/rdr2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("RDR2.html", {"request": request})

@router.get("/valheim")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Valheim.html", {"request": request})

@router.get("/ark")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("ARK.html", {"request": request})

@router.get("/god_of_war")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("God_of_War.html", {"request": request})


@router.get("/god_of_war_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("God_of_War_2.html", {"request": request})

@router.get("/factorio")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Factorio.html", {"request": request})

@router.get("/dishonored")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Dishonored.html", {"request": request})

@router.get("/dishonored_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Dishonored_2.html", {"request": request})

@router.get("/papers")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Papers_Please.html", {"request": request})

@router.get("/spyro")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Spyro.html", {"request": request})

@router.get("/ace_attorney")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Ace_Attorney.html", {"request": request})

@router.get("/fear_and_hunger")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Fear_And_Hunger.html", {"request": request})

@router.get("/fear_and_hunger_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Fear_And_Hunger_2.html", {"request": request})

@router.get("/dmc5")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("DMC5.html", {"request": request})

@router.get("/meatboy")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Super_Meatboy.html", {"request": request})

@router.get("/star_wars")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Star_Wars.html", {"request": request})

@router.get("/star_wars_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Star_Wars_2.html", {"request": request})

@router.get("/danganronpa")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Danganronpa.html", {"request": request})

@router.get("/control")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Control.html", {"request": request})

@router.get("/dead_cells")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Dead_Cells.html", {"request": request})

@router.get("/evil_within")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Evil_Within.html", {"request": request})

@router.get("/evil_within_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Evil_Within_2.html", {"request": request})

@router.get("/sifu")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Sifu.html", {"request": request})

@router.get("/yuppie")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Yuppie_Phycho.html", {"request": request})

@router.get("/outcore")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Outcore.html", {"request": request})

@router.get("/dying_light")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Dying_Light.html", {"request": request})

@router.get("/dying_light_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Dying_Light_2.html", {"request": request})

@router.get("/atomic_heart")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Atomic_Heart.html", {"request": request})

@router.get("/long_dark")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Long_Dark.html", {"request": request})

@router.get("/project_zomboid")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Project_Zomboid.html", {"request": request})

@router.get("/farming")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Farming.html", {"request": request})

@router.get("/overwatch")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Overwatch.html", {"request": request})

@router.get("/spider_man")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Spider_Man.html", {"request": request})

@router.get("/spider_man_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Spider_Man_2.html", {"request": request})

@router.get("/alan_wake")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Alan_Wake.html", {"request": request})

@router.get("/buckshoot_roulette")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Buckshoot_Roulette.html", {"request": request})

@router.get("/bioshock")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("BioShock.html", {"request": request})

@router.get("/bioshock_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("BioShock_2.html", {"request": request})

@router.get("/mirror’s_edge")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mirror’s_Edge.html", {"request": request})

@router.get("/left_4_dead")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Left_4_Dead.html", {"request": request})

@router.get("/left_4_dead_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Left_4_Dead_2.html", {"request": request})

@router.get("/dead_space")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Dead_Space.html", {"request": request})

@router.get("/dead_space_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Dead_Space_2.html", {"request": request})

@router.get("/watch_dogs")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Watch_Dogs.html", {"request": request})

@router.get("/watch_dogs_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Watch_Dogs_2.html", {"request": request})

@router.get("/watch_dogs_legion")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Watch_Dogs_Legion.html", {"request": request})

@router.get("/world_of_tanks")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("World_of_Tanks.html", {"request": request})

@router.get("/limbo")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Limbo.html", {"request": request})

@router.get("/borderlands")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Borderlands.html", {"request": request})

@router.get("/borderlands_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Borderlands_2.html", {"request": request})

@router.get("/borderlands_3")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Borderlands_3.html", {"request": request})

@router.get("/titan_quest")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Titan_Quest.html", {"request": request})

@router.get("/heavy_rain")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Heavy_Rain.html", {"request": request})

@router.get("/zombies")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Zombies.html", {"request": request})

@router.get("/cs_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("CS_2.html", {"request": request})

@router.get("/lineage_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Lineage_2.html", {"request": request})

@router.get("/ori")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Ori.html", {"request": request})

@router.get("/bully")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Bully.html", {"request": request})

@router.get("/life_is_strange")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Life_Is_Strange.html", {"request": request})

@router.get("/quake")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Quake.html", {"request": request})

@router.get("/quake_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Quake_2.html", {"request": request})

@router.get("/quake_3")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Quake_3.html", {"request": request})

@router.get("/quake_4")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Quake_4.html", {"request": request})

@router.get("/south_park")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("South_Park.html", {"request": request})

@router.get("/among_us")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Among_Us.html", {"request": request})

@router.get("/payday")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("PayDay.html", {"request": request})

@router.get("/payday_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("PayDay_2.html", {"request": request})

@router.get("/payday_3")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("PayDay_3.html", {"request": request})

@router.get("/worms")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Worms.html", {"request": request})

@router.get("/beyond")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Beyond.html", {"request": request})

@router.get("/dayz")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("DayZ.html", {"request": request})

@router.get("/no_man's_sky")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("No_Man's_Sky.html", {"request": request})

@router.get("/rainbow_six")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Rainbow_Six.html", {"request": request})

@router.get("/mafia")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mafia.html", {"request": request})

@router.get("/mafia_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mafia_2.html", {"request": request})

@router.get("/mafia_3")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mafia_3.html", {"request": request})

@router.get("/mafia_def")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mafia_Definitive_Edition.html", {"request": request})

@router.get("/plague_tale")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Plague_Tale.html", {"request": request})

@router.get("/plague_tale_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Plague_Tale_2.html", {"request": request})

@router.get("/escapists")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Escapists.html", {"request": request})

@router.get("/halo")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Halo.html", {"request": request})

@router.get("/halo_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Halo_2.html", {"request": request})

@router.get("/halo_3")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Halo_3.html", {"request": request})

@router.get("/halo_4")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Halo_4.html", {"request": request})

@router.get("/halo_infinite")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Halo_Infinite.html", {"request": request})

@router.get("/rocket_league")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Rocket_League.html", {"request": request})

@router.get("/crossout")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Crossout.html", {"request": request})

@router.get("/hello_neighbor")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Hello_Neighbor.html", {"request": request})

@router.get("/hello_neighbor_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Hello_Neighbor_2.html", {"request": request})

@router.get("/path_of_exile")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Path_of_Exile.html", {"request": request})

@router.get("/unravel")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Unravel.html", {"request": request})

@router.get("/unravel_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Unravel_2.html", {"request": request})

@router.get("/leos_fortune")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Leos_Fortune.html", {"request": request})

@router.get("/lucky_tower")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Lucky_Tower.html", {"request": request})

@router.get("/everlasting_summer")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Everlasting_Summer.html", {"request": request})

@router.get("/cult")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Cult_of_the_Lamb.html", {"request": request})

@router.get("/plague_inc")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Plague_Inc.html", {"request": request})

@router.get("/doki_doki")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Doki_Doki.html", {"request": request})

@router.get("/hotline")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Hotline_Miami.html", {"request": request})

@router.get("/outlast")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Outlast.html", {"request": request})

@router.get("/outlast_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Outlast_2.html", {"request": request})

@router.get("/hades")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Hades.html", {"request": request})

@router.get("/hades_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Hades_2.html", {"request": request})

@router.get("/rayman")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Rayman.html", {"request": request})

@router.get("/uncharted")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Uncharted.html", {"request": request})

@router.get("/goat")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Goat.html", {"request": request})

@router.get("/disco")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Disco.html", {"request": request})

@router.get("/superhot")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Superhot.html", {"request": request})

@router.get("/abzu")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("ABZU.html", {"request": request})

@router.get("/it_takes_two")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("it_takes_two.html", {"request": request})





