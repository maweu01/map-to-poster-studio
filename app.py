import os
import glob
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from create_map_poster import create_poster

app = FastAPI(title="Map Poster Generator API")

@app.get("/generate")
async def generate_poster_endpoint(
    city: str = Query(..., description="City name"),
    country: str = Query(..., description="Country name"),
    theme: str = Query("midnight_blue", description="Theme name"),
    distance: int = Query(15000, description="Radius in meters")
):
    try:
        # Fixed parameter mapping here: passing theme=theme
        create_poster(city=city, country=country, theme=theme, dist=distance)
        
        # Locate the generated file structure inside /posters
        out_dir = "posters"
        list_of_files = glob.glob(os.path.join(out_dir, '*.png'))
        if not list_of_files:
            raise HTTPException(status_code=500, detail="Poster generation failed to save.")
            
        # Find the absolute newest file generated
        latest_file = max(list_of_files, key=os.path.getctime)
        return FileResponse(latest_file, media_type="image/png")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
EOFcat << 'EOF' > app.py
import os
import glob
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from create_map_poster import create_poster

app = FastAPI(title="Map Poster Generator API")

@app.get("/generate")
async def generate_poster_endpoint(
    city: str = Query(..., description="City name"),
    country: str = Query(..., description="Country name"),
    theme: str = Query("midnight_blue", description="Theme name"),
    distance: int = Query(15000, description="Radius in meters")
):
    try:
        # Fixed parameter mapping here: passing theme=theme
        create_poster(city=city, country=country, theme=theme, dist=distance)
        
        # Locate the generated file structure inside /posters
        out_dir = "posters"
        list_of_files = glob.glob(os.path.join(out_dir, '*.png'))
        if not list_of_files:
            raise HTTPException(status_code=500, detail="Poster generation failed to save.")
            
        # Find the absolute newest file generated
        latest_file = max(list_of_files, key=os.path.getctime)
        return FileResponse(latest_file, media_type="image/png")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
EOFcat << 'EOF' > app.py
import os
import glob
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from create_map_poster import create_poster

app = FastAPI(title="Map Poster Generator API")

@app.get("/generate")
async def generate_poster_endpoint(
    city: str = Query(..., description="City name"),
    country: str = Query(..., description="Country name"),
    theme: str = Query("midnight_blue", description="Theme name"),
    distance: int = Query(15000, description="Radius in meters")
):
    try:
        # Fixed parameter mapping here: passing theme=theme
        create_poster(city=city, country=country, theme=theme, dist=distance)
        
        # Locate the generated file structure inside /posters
        out_dir = "posters"
        list_of_files = glob.glob(os.path.join(out_dir, '*.png'))
        if not list_of_files:
            raise HTTPException(status_code=500, detail="Poster generation failed to save.")
            
        # Find the absolute newest file generated
        latest_file = max(list_of_files, key=os.path.getctime)
        return FileResponse(latest_file, media_type="image/png")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
