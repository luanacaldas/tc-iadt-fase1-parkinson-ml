# Detecção de Parkinson por Análise de Voz

Sistema de Machine Learning para detecção da Doença de Parkinson através de características acústicas da voz.

## 📊 Resultados

| Modelo | F1-Score | Precisão | Recall |
|--------|----------|----------|--------|
| Regressão Logística | 0.850 | 0.870 | 0.830 |
| Random Forest | 0.920 | 0.910 | 0.930 |
| **XGBoost** | **0.934** | **0.940** | **0.930** |

## 🚀 Início Rápido

```bash
# Clone o repositório
git clone https://github.com/luanacaldas/tc-iadt-fase1-parkinson-ml.git
cd tc-iadt-fase1-parkinson-ml

# Instale dependências
pip install -r requirements.txt

# Execute o notebook
jupyter notebook TC_1_fiap.ipynb
```

Ou acesse direto no [Google Colab](https://colab.research.google.com/github/luanacaldas/tc-iadt-fase1-parkinson-ml/blob/main/TC_1_fiap.ipynb)

## 📁 Dataset

- **Fonte**: UCI Machine Learning Repository
- **Amostras**: 195 gravações (23 com Parkinson, 8 saudáveis)
- **Features**: 22 características acústicas biomédicas

## 🛠️ Tecnologias

- Python 3.8+
- scikit-learn, XGBoost
- SHAP (interpretabilidade)
- pandas, matplotlib, seaborn

## 📈 Metodologia

1. **Análise Exploratória**: Correlação, distribuição de classes
2. **Pré-processamento**: Padronização, divisão estratificada (80/20)
3. **Modelagem**: 3 algoritmos com validação cruzada 5-fold
4. **Interpretabilidade**: SHAP values para explicabilidade
5. **Avaliação**: Matriz de confusão, curva ROC, análise de erros

## 🎯 Features Mais Importantes

1. **spread1** (29.8%) - Variação não-linear da frequência
2. **PPE** (18.2%) - Entropia de pitch
3. **spread2** (12.4%) - Variação de frequência complementar
4. **MDVP:Fo** (8.7%) - Frequência fundamental média
5. **HNR** (6.9%) - Harmonic-to-Noise Ratio

## ⚠️ Limitações

- Dataset pequeno (195 amostras)
- Desbalanceamento de classes (75% Parkinson)
- Sem validação externa
- Ausência de dados demográficos e estágio da doença

## 📝 Estrutura do Projeto

```
tc-iadt-fase1-parkinson-ml/
├── TC_1_fiap.ipynb       # Notebook principal
├── tc_1_fiap.py          # Script Python
├── README.md             # Documentação
└── requirements.txt      # Dependências
```

## 👥 Autores

**Luana Caldas** & **Elaine Martins da Silva**  
FIAP - Tech Challenge Fase 1  
Orientação: Prof.ª Poliana Nascimento Ferreira

## 📚 Referências

- Little et al. (2009) - [BioMedical Engineering OnLine](https://doi.org/10.1186/1475-925X-6-23)
- Tsanas et al. (2012) - [IEEE TBME](https://doi.org/10.1109/TBME.2012.2183367)
- [UCI ML Repository - Parkinsons Dataset](https://archive.ics.uci.edu/ml/datasets/parkinsons)

## ⚕️ Aviso

**Este modelo é uma ferramenta de apoio à decisão clínica e NÃO substitui o diagnóstico médico especializado.**

## 📄 Licença

MIT License
