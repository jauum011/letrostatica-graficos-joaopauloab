import matplotlib.pyplot as plt

k = 8.99e9   
q = 1

distancias = [0.10 + i * 0.01 for i in range(91)]
forcas = [k * abs(q) / (r ** 2) for r in distancias]

plt.figure(figsize=(6, 4))
plt.plot(distancias, forcas, color="tab:blue", linewidth=2)
plt.title("Campo Elétrico vs. Distância (Lei de Coulomb)")
plt.xlabel("Distância r (m)")
plt.ylabel("Força F (N)")
plt.grid(True)
plt.tight_layout()
plt.savefig("campo_coulomb.png", dpi=150)
print("Gráfico salvo em forca_coulomb.png!")