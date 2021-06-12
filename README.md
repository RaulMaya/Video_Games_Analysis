# ETL Project
## Extract, Transform and Load videogames data

### Contributors
* Edoardo Zapata
* Juan Francisco Camberos
* Raúl Maya
* Ricardo Pérez
* Salvador del Cos Garza

### Project Description/Outline

The scope of this project is to extract data from different data sources, clean and transform them and load them into a database in order to solve specific queries. This project was developed using Python, Pandas, MongoDB and PyMongo. Data was retrieved from two sources: [dataworld.com](https://data.world/sumitrock/videogames) for Console games and [kaggle.com](https://www.kaggle.com/nikdavis/steam-store-games) for Steam games.

### Executive Report

Executive report for this project can be found [here](https://docs.google.com/document/d/1nvgadoA2MatHyb9iYDkm12OfAQX9vca38SyVaIQAQ4U/edit?usp=sharing).


### WorkFlow

#### 1. Extract Data
Datasets were downloaded in CSV format and then imported into Pandas DataFrame: 

| Raw data for Console & Steam games |
| --- |
| ![Console](images/Console_Raw.png) |
| ![Steam](images/Steam_Raw.png) |

#### 2. Transformed Data
After exploring raw data, datasets were cleaned and formatted (select relevant fields, cast types, compute missing fields, rename columns, etc.): 

| Clean data for Console & Steam games |
| --- |
| ![Console](images/Console_Clean.png) |
| ![Steam](images/Steam_Clean.png) |

#### 3. Load Data
The team decided to use a NoSQL Database (MongoDB) as the best fit in order to solve queries since the data gathered had relevant fields with mixed types (int, NaN, str) ; the team felt it was more safe to use Mongo’s JSON format to store the data. 

There was no need to use mapping of application objects to database objects in  MongoDB. And the document query language supported by mongo is simpler compared to SQL queries. 




| MongoDB `united` collection |
| --- |
| ![Console](images/MongoDB.png) |

