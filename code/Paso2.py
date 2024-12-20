{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a89129f-3aad-4b81-8c46-88dabbb7d81e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def segmentacion_hounsfield(volumen):\n",
    "    aire = (-1000, -900)\n",
    "    pulmon = (-900, -500)\n",
    "    tejido_adiposo = (-500, -50)\n",
    "    agua = (-50, 50)\n",
    "    tejido_blando = (50, 500)\n",
    "    hueso = (500, 1000)\n",
    "\n",
    "    mascara_aire = (volumen >= aire[0]) & (volumen < aire[1])\n",
    "    mascara_pulmon = (volumen >= pulmon[0]) & (volumen < pulmon[1])\n",
    "    mascara_tejido_adiposo = (volumen >= tejido_adiposo[0]) & (volumen < tejido_adiposo[1])\n",
    "    mascara_agua = (volumen >= agua[0]) & (volumen < agua[1])\n",
    "    mascara_tejido_blando = (volumen >= tejido_blando[0]) & (volumen < tejido_blando[1])\n",
    "    mascara_hueso = (volumen >= hueso[0]) & (volumen <= hueso[1])\n",
    "\n",
    "    segmentacion = np.zeros_like(volumen)\n",
    "    segmentacion[mascara_aire] = 1\n",
    "    segmentacion[mascara_pulmon] = 2\n",
    "    segmentacion[mascara_tejido_adiposo] = 3\n",
    "    segmentacion[mascara_agua] = 4\n",
    "    segmentacion[mascara_tejido_blando] = 5\n",
    "    segmentacion[mascara_hueso] = 6\n",
    "\n",
    "    return segmentacion\n",
    "\n",
    "def segmentacion_otsu(volumen):\n",
    "    volumen_norm = (volumen - volumen.min()) / (volumen.max() - volumen.min())\n",
    "    thresholds = filters.threshold_multiotsu(volumen_norm, classes=3)  # Cambia a 3 para pruebas\n",
    "    segmentacion = np.digitize(volumen_norm, bins=thresholds)\n",
    "    return segmentacion\n",
    "\n",
    "def visualizar_segmentacion(volumen, segmentacion_hu, segmentacion_otsu):\n",
    "    # Seleccionar un corte central para visualización\n",
    "    corte = volumen.shape[2] // 2\n",
    "   \n",
    "    fig, axs = plt.subplots(2, 2, figsize=(10, 10))\n",
    "   \n",
    "    # Mostrar imagen original\n",
    "    axs[0, 0].imshow(volumen[:, :, corte], cmap='gray',aspect='auto') #auto para asegurar que usamos la relacion aspecto correcta\n",
    "    axs[0, 0].set_title('Imagen Original')\n",
    "    axs[0, 0].axis('off')\n",
    "   \n",
    "    # Mostrar segmentación Hounsfield\n",
    "    axs[0, 1].imshow(segmentacion_hu[:, :, corte], cmap='jet', aspect='auto')\n",
    "    axs[0, 1].set_title('Segmentación Hounsfield')\n",
    "    axs[0, 1].axis('off')\n",
    "   \n",
    "    # Mostrar histograma\n",
    "    axs[1, 0].hist(volumen[:, :, corte].ravel(), bins=256)\n",
    "    axs[1, 0].set_title('Histograma')\n",
    "    axs[1, 0].set_xlabel('Valor de píxel')\n",
    "    axs[1, 0].set_ylabel('Frecuencia')\n",
    "\n",
    "    # Mostrar segmentación Otsu\n",
    "    axs[1, 1].imshow(segmentacion_otsu[:, :, corte], cmap='jet', aspect='auto')  \n",
    "    axs[1, 1].set_title('Segmentación Otsu')\n",
    "    axs[1, 1].axis('off')\n",
    "\n",
    "    plt.tight_layout()\n",
    "    plt.show()\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.20"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
