{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ecf56613-b07b-44da-bb5c-f0e70baaa4f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def MuestraVolumen(volumen, img_shape, relacion_aspecto, voxel_size, mostrar_histograma = False):\n",
    "    #Calculamos el corte medio para cada orientación\n",
    "    \n",
    "    corte_medio_axial = volumen.shape[2] // 2\n",
    "    corte_medio_coronal = volumen.shape[0] // 2\n",
    "    corte_medio_sagital = volumen.shape[1] // 2\n",
    "    \n",
    "    \n",
    "    fig, axes = plt.subplots(ncols = 2, nrows = 2, figsize =(10, 10))\n",
    "    ax = axes.ravel()\n",
    "    \n",
    "    #CORTE MEDIO AXIAL\n",
    "    imagen_axial = volumen[:,:, corte_medio_axial]\n",
    "    ax[2].imshow(imagen_axial, cmap=plt.cm.gray)\n",
    "    ax[2].set_title(f\"Corte axial:{corte_medio_axial}\")\n",
    "    ax[2].axis(\"off\")\n",
    "    ax[2].set_aspect(relacion_aspecto[0])\n",
    "    #axial_aspect = relacion_aspecto[0]*voxel_size[0]\n",
    "    #ax[0].set_aspect(axial_aspect)\n",
    "\n",
    "    #CORTE MEDIO CORONAL\n",
    "    imagen_coronal = volumen[corte_medio_coronal, :, :].T\n",
    "    ax[0].imshow(imagen_coronal, cmap=plt.cm.gray)\n",
    "    ax[0].set_title(f\"Corte coronal:{corte_medio_coronal}\")\n",
    "    ax[0].axis(\"off\")\n",
    "    ax[0].set_aspect(relacion_aspecto[2])\n",
    "    #coronal_aspect = relacion_aspecto[1]*voxel_size[1]\n",
    "    #ax[1].set_aspect(coronal_aspect)\n",
    "\n",
    "    #CORTE MEDIO SAGITAL\n",
    "    imagen_sagital = volumen[:,corte_medio_sagital, :].T\n",
    "    ax[1].imshow(imagen_sagital, cmap=plt.cm.gray)\n",
    "    ax[1].set_title(f\"Corte sagital:{corte_medio_sagital}\")\n",
    "    ax[1].axis(\"off\")\n",
    "    ax[1].set_aspect(relacion_aspecto[1])\n",
    "    #sagital_aspect = relacion_aspecto[2]*voxel_size[2]\n",
    "    #ax[2].set_aspect(sagital_aspect)\n",
    "\n",
    "    #HISTOGRAMA\n",
    "    if mostrar_histograma == True:\n",
    "        histogram_256, bin_edges_256 = np.histogram(volumen, bins=256, range=(np.min(volumen),np.max(volumen)))\n",
    "        ax[3].plot(bin_edges_256[0:-1], histogram_256)\n",
    "        ax[3].set_title('Histograma en escala de grises de la imagen original')\n",
    "        ax[3].set_xlabel(\"Unidades Hounsfield\")\n",
    "        ax[3].set_ylabel(\"Número de píxeles\")\n",
    "        ax[3].set_xlim([-2000.0, 1000.0]) \n",
    "        \n",
    "    plt.tight_layout()\n",
    "    plt.show()"
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
