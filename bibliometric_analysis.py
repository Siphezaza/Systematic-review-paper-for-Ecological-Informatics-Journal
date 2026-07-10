"""
bibliometric_analysis.py

Bibliometric analyses for the systematic review:
  (1) Word cloud of author keywords (Figure 10b)
  (2) Geographic distribution of first-author affiliations by method (Figure 9)

Extracted from the project analysis notebook (full_analysis_notebook.py).

Requirements:
    pip install wordcloud matplotlib geopandas pandas

Inputs:
    studies_affiliation.xlsx   (columns: AffiliationLon, AffiliationLat, Method)
                               required only for the affiliation map.
"""

# ==========================================================================
# (1) KEYWORD WORD CLOUD  (Figure 10b)
# ==========================================================================
from wordcloud import WordCloud

# your long text string
text = """Cycles; Ecological network analysis; Eigenvalue; Food-web; Hierarchy; Indirect effects; Modularity; Network analysis; Network environ analysis; Spectral radius; Dominator tree; Energy flow; Food web; Graph theory; Secondary extinction; Acoustic telemetry; Coral reef resilience; Ecosystem function; Parrotfishes; Rabbitfishes; Roving herbivores; Small-world networks; Spatial ecology; Connectivity; Fish; Landscape ecology; Pattern metrics; Seascape ecology; Spatial-scale; Dendritic networks; Ecological networks; Fragmentation; Graph theory; Spatial graphs; Stream network; Community detection; Coral; Graph theory; Great Barrier Reef; Larval dispersal; Marine connectivity; Giant kelp; Landsat; Metapopulation; Modularity; Network; Patch dynamics; Remote sensing; Spatial autocorrelation; Synchrony; Dispersal; Graph theory; Habitat fragmentation; Landscape ecology; Latent space models; Centrality measures; Clustering methods; Communicability; Estrada index; Fiedler vector; Graph Laplacian; Graph spectrum; Power series; Resolvent; Conservation; Dispersal; Management; Modeling; Population genetics; Review; Spatial ecology; Tracking; Connectivity; Marine conservation planning; Marine larvae dispersal; Marine metapopulation model; Marine reserves; Graph theory; Gulf of California; Larval dispersal; Marine connectivity; Marine Life Protection Act; Marine protected areas networks; Rules of thumb; Spacing rules. Coral dispersal; Networks; Seriatopora hystrix; Small world topology; biological fluid dynamics; flow control; swimming/flying; Directed graphs; Food webs; Graph theory; Network ecology; Fragmentation; Graph theory; Submersed aquatic vegetation; biological network; graph theory; sharks; trophic interactions; truncated power-law; connectivity; conservation planning; coral reef; fish movement; marine conservation; marine reserves; network model; seascape; Connectivity analysis; Graph theory; Marine conservation planning; MARXAN; Multivariate analyses; Colombian Pacific; Ecosystems; Food webs; Graph theory; Interspecific relationships; Trophic structure; anthropogenic stressors; aquatic ecosystems; ecological networks; functional connectivity; landscape connectivity; metapopulation dynamics. ecological network; ecological process; Gulf of California; larval dispersal; marine conservation; marine reserve network; ocean warming; systematic conservation planning; Acanthaster planci; Cluster coefficient; Connectivity; Graph theory; Water quality; Ecological function; Graph theory; Grazing; Network theory; Resilience; Caribbean; Connectivity; Dispersal; Fish larvae; Gyres; Honduras gyre; Larval dispersal; Marine protected area; Mesoamerican Barrier Reef; Seasonal; Spawning aggregation; Yucatan current; British Columbia; ecological connectivity; graph theory; habitat proxy; marine conservation; marine reserve; marine spatial planning; multiplex network; network analysis; Northern Shelf Bioregion; population connectivity; Deep learning; Ecosystem service bundles; Eudaimonia; Graph theory network analysis; Marine and coastal areas; Relational values; genetic connectivity; Mediterranean Sea; Mullus surmuletus; seascape genetics; spatial graphs; stepping-stone dispersal; biophysical modeling; connectivity; Florida reef tract; spatial epidemiology; stony-coral-tissue-loss disease; biophysical modeling; connectivity; coral reef larvae; dispersal; graph theory analysis; connectivity; cumulative effects; graph theory; Great Barrier Reef; networks; seagrass; areas beyond national jurisdiction; fisheries management; functional connectivity; high seas; larval dispersal; marine conservation planning; marine protected areas; ocean governance; regional MPA; seafloor geomorphic habitats; Western Indian Ocean; Connectivity; Graph theory; Marine protected area networks; Markov Chain Monte Carlo; Multi-objective optimization; Pareto optimal solution; Random geometric graph; Biodiversity conservation; Biophysical modelling; Connectivity; Marine biodiversity; Marine protected areas; Networks of marine protected areas; degree centrality; eigenvalue; eigenvector; larval dispersal; network analysis; out-degree; resilience; self-recruitment; Biophysical model; Connectivity; Dispersal; Individual based models; Lagrangian particles; Seagrass; Benthic communities; Bipartite networks; Graph theory; Maërl beds; Mediterranean; Species richness; Allee effect; Langrangian model; larval dispersal; metapopulation; population connectivity; queen conch; Balearic Islands; Connectivity; Graph theory; Individual-based models; NW Mediterranean Sea; Posidonia oceanica; Restoration; Seagrass; Seed dispersal; conectividad; connectivity; diseño de reservas marinas; dispersión larval; graph theory; larval dispersal; marine reserve design; Marxan; Marxan; planeación sistemática de la conservación; systematic conservation planning; teoría de gráficos; Conservation; Ecological network; Food web; Marine ecosystem; Network-based; Coastal habitats; Coastal management; Ecosystem functions; Ecosystems services; Social actors; biodiversity conservation; marine protected areas (MPAs); propagule dispersal; recruitment; resource management; stepping-stone; betweenness centrality; graph theory; habitat fragmentation; hydrodynamic modelling; larval dispersal; network analysis; resilience; gene flow; genetic differentiation; long-distance dispersal; macroalgae; macrogenetics; multigeneration connectivity; stepping stone; Community stability; Community variation; Conservation area; Graph kernel; Reef fish community; Symbiotic graph model; Ecosystem dynamics; Graph neural network; Mesozooplankton; Transfer entropy; beta-diversity; biogeography; conservation; endemism; faunal distribution; hydrothermal vent; network connectivity; seabed mining; western Pacific; Artificial upwelling; Carbon sequestration; Deep reinforcement learning; Energy management; Biophysical modelling; Connectivity; Graph theory; Invasive species; Larval dispersal; Magallana gigas; Coral dispersal; Graph theory; Marine protected areas; Networks; Tropical Pacific; Recruitment; Marine environment; Larvae; Connectivity; Dispersal; Semibalanus; Recolonization; Barnacle; animal movement; behavioral monitoring; bio-logging; biotelemetry; Calonectris leucomelas; habitat selection; interpolation; inverse reinforcement learning; machine learning; reward map; tracking data. Larval connectivity; MPA network; Larval dispersal; Larval transport; Management; Betweenness; Centrality; Closeness; Graph theory; Marine turtle; Migratory; Satellite telemetry; Tracking; Acoustic tagging; Fish movement; Social network analysis; Bipartite graphs; Directed graphs; Biophysical models; Population genetics; Oceanography; Gulf of California; Fisheries; No-take zones; Marine reserves; Larval dispersal; Marine connectivity; Small world; Coral reefs; Scale free; Graph theory; Metapopulation; Acoustic telemetry; Coral reef resilience; Ecosystem function; Parrotfishes; Rabbitfishes; Roving herbivores; Small-world networks; Spatial ecology; Centrality measures; Fragmented habitat; Graph theory; Machine learning; Predictive model; Seascape connectivity; Conservation planning; Local retention; Metapopulation persistence; Network metrics; Network theory; Reserve networks; Self-recruitment; Biogeography; Microbial diversity; High-throughput sequencing; Environmental rDNA sequencing; Protist; Metapopulation; Dispersal; Networks; Graph theory; Larval dispersal; Connectivity; Dynamic energy budget; Graph-theory; Network; Larval dispersal; Connectivity; Agent-based modelling; Cockles; Cerastoderma edule; Limfjorden; Biogeography; Connectivity; Hydrothermal vent; Metacommunity; Network; Foodweb; Harmful algal blooms; Networks; Overfishing; Trophic cascade; Metapopulations; Coral reefs; Graph theory; Small world; Topology; Conservation planning; Artificial intelligence; Automation; Ecological monitoring; Marine conservation; Conservation management; Machine learning; Restoration; Lagrangian particle tracking; Graph-theoretic metric; Shannon index; Vertex degree; Betweenness centrality; Potential connectivity; Marine connectivity; Larval dispersal; Marine protected areas; Hawaiian archipelago; Biophysical modelling; Microswimmer; Turbulent flow; Optimal navigation; Diel vertical migration; Reinforcement learning; marine oil spill monitoring; graph neural network; semantic segmentation; Swin-Unet; Graph-DeeplabV3+;  sea surface temperature; non-uniform grid; spatiotemporal prediction; graph neural network; hyperspectral remote sensing; oil spill type identification; oil film thickness detection; multilevel spatial and spectral feature; deep learning

"""

# split on semicolon and strip spaces
tokens = [t.strip() for t in text.split(";") if t.strip()]

# join tokens with space (so each phrase is treated as one "word")
processed_text = " ".join(tokens)

# generate word cloud
wc = WordCloud(width=1200, height=800, collocations=False).generate(processed_text)

# show
import matplotlib.pyplot as plt
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()


# ==========================================================================
# (2) FIRST-AUTHOR AFFILIATION MAP BY METHOD  (Figure 9)
# ==========================================================================
import geopandas as gpd
import matplotlib.pyplot as plt

# === 1. Load your Excel file ===
df = pd.read_excel("studies_affiliation.xlsx")

# === 2. Convert to GeoDataFrame ===
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["AffiliationLon"], df["AffiliationLat"]),
    crs="EPSG:4326"
)

# === 3. Load world shapefile from Natural Earth ===
world = gpd.read_file("https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip")

# === 4. Plot ===
fig, ax = plt.subplots(figsize=(12, 6))
world.boundary.plot(ax=ax, linewidth=0.8, color="black")

method_colors = {"GT": "blue", "RL": "red", "GNN": "green"}
for method, group in gdf.groupby("Method"):
    group.plot(ax=ax, markersize=80, marker="o",
               color=method_colors.get(method, "gray"),
               label=method, alpha=0.7)

plt.title("Geospatial Distribution of First Author Affiliations (RL, GT, GNN)", fontsize=14)

# Legend outside
plt.legend(
    title="Method",
    bbox_to_anchor=(1.05, 1),   # position legend outside
    loc="upper left",           # anchor point
    borderaxespad=0
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.savefig("affiliation_map.png", dpi=300, bbox_inches="tight")
plt.show()

