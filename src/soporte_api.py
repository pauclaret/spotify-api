import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
load_dotenv()
import math

def credenciales():
    client_secret = os.getenv("secret")
    client_id = os.getenv("id")
    print(client_id)
    print(client_secret)
    credenciales = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=credenciales)
    return sp

def sacar_canciones(url, num_canciones, conexion):
    uri = url.split("/")[-1].split("?")[0]
    offset = 0
    resultados = []
    for i in range(num_canciones):
        resultados.append(conexion.playlist_tracks(uri, offset = offset)["items"])
        offset += 100
    return resultados

    
def sacar_numero_canciones(num_canciones_input):
    num_canciones_input = int(num_canciones_input)
    
    if num_canciones_input < 100:
        return 1
    else:
        num_canciones_input /= 100
        return math.ceil(num_canciones_input)
    
def limpiar_datos(resultados):
    basic_info = {"song": [], "artist": [], "date": [], "explicit": [], "uri": [], "popularity": [], "usuario": [], "links": [], 'uri_artista': []}
    for i in range(len(resultados)): 
        for z in range(len(resultados[i])): 
            artista = []
            uris = []

            basic_info["uri"].append(resultados[i][z]["track"]["uri"])
            basic_info["song"].append(resultados[i][z]["track"]["name"])
            basic_info["date"].append(resultados[i][z]["track"]["album"]["release_date"])
            basic_info["explicit"].append(resultados[i][z]["track"]["explicit"])
            basic_info["popularity"].append(resultados[i][z]["track"]["popularity"])
            basic_info["usuario"].append(resultados[i][z]["added_by"]["id"])
            basic_info["links"].append(resultados[i][z]["track"]["external_urls"]["spotify"])

            
            if len(resultados[i][z]["track"]["artists"]) == 1:
                basic_info["artist"].append(resultados[i][z]["track"]["artists"][0]["name"])
                basic_info["uri_artista"].append(resultados[i][z]["track"]["artists"][0]["id"])

            else:
                for x in range(len(resultados[i][z]["track"]["artists"])):
                    artista.append(resultados[i][z]["track"]["artists"][x]["name"])
                    uris.append(resultados[i][z]["track"]["artists"][x]["id"])
                basic_info["artist"].append(artista)
                basic_info["uri_artista"].append(uris)
                
        df = pd.DataFrame(basic_info)
        mapa = {"1129644679": "Pau", 
        "alvarogcambronero": "Elisa", 
        "1183037273": "Ana", 
        "annxox": "Ana S", 
        "belen.gasset": "Belén", 
        "8epi76oaztyef2ws47q0lwcuz": "Amiga de Pau", 
        "11159625835": "Jorge", 
        "115724470": "Sindri", 
        "miriamplz": "Miriam",
        "4bkhftxifirml76m9kdv5m8tf": "Ana G", 
        "1180927307": "Paula",
        "2177d6zcret6mozpaakgowcna": "Lin", 
        "31usc6kzxaks4tdjv262fanxtxka": "Brandon"}
        
        df["usuario"] = df["usuario"].map(mapa)
        return df

def sacar_big_numbers(df):
    df = df.explode("artist")

    num_canciones = len(df["song"].unique())
    num_artistas = len(df["artist"].unique())
    num_usuarios = len(df["usuario"].unique())
    return num_canciones, num_artistas, num_usuarios

