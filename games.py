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


