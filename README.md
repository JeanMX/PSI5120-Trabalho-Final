# Repositório para o trabalho final da matéria PSI5120

## Pré-requisitos para todos os casos

Para a realização de quaisquer casos, será necessário algumas configurações.

Primeiramente, é necessário criar uma [conta no AWS](https://aws.amazon.com/getting-started/guides/setup-environment/).

será necessário criar um domínio no SageMaker Studio atrvés do [AWS CloudFormation stack](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://ws-assets-prod-iad-r-iad-ed304a55c2ca1aee.s3.us-east-1.amazonaws.com/80ba0ea5-7cf9-4b8c-9d3f-1cd988b6c071/cfn-templates/domain_canvas.yaml), confirme que a região da sua onta do AWS é US East (N. Virginia). Coloque o nome do stack como: "CFN-SM-IM-Lambda-catalog".

Importante: Para a criação desse stack é necessário um VPC público configurado na sua conta, caso não tenha configure usando esse [tutorial](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-dev-test.html).

Durante a criação do stack selecione: "I acknowledge that AWS CloudFormation might create IAM resources", e escolha Create stack.

O processo de criação do stack pode levar até 10 minutos, mudando o estado de CREATE_IN_PROGRESS para CREATE_COMPLETE.

## Caso 1: Básico

O primeiro caso tem como objetivo utilizar o Sagemaker para criar automaticamente modelos de aprendizado de máquina. Nessa etapa, não é necessário nenhum tipo de código fonte, sendo necessário apenas seguir um passo a passo dentro da plataforma do AWS.

Pré-requisitos
- SageMaker Canvas

No SageMaker Canvas vá em "My Models" e clique em "Create new model". Coloque o nome do modelo como Marketing Campaign, selecione o Problem type como "Predictive analysis" e crie o modelo.

Em Select dataset vá em "+ Create dataset". Nomeie o dataset como "MarketingData" e clique em create.

Baixe o dataset nesse [link](https://sagemaker-sample-files.s3.amazonaws.com/datasets/tabular/uci_bank_marketing/bank-additional-full.csv). Após o download em sua máquina local, vá em Local upload e arraste o arquivo bank-additional-full.csv, que foi baixado em sua máquina. Clicando em Preview dataset, é possível observar o dataset importado na interface do SageMaker, estando tudo certo, clique em "Create dataset".

Tendo o dataset importante, clique no botão ao lado do "MarketingData" e clique para selecionar o dataset, selecionando o que foi importado.

Na coluna de target, selecione a coluna "y" e clique na seta para baixo para a criação rápida do build. Vá em Configure model, nessa parte é possível configurar quais métricas você deseja adquirir do modelo. Em Data Split, coloque 80% para treinamento e 20% para validação. Na aba Max candidates and runtime, coloque o Max job runtime em 30 minutos, para garantir que tenha tempo suficiente para o treinamento completo.

Após essas configurações, clique em Standard build e o treinamento irá iniciar, levando 45 minutos aproximadamente para finalizar. 

Na pasta básico desse repositório, há um documento com capturas de tela do resultado do treinamento e da validação.


## Caso 2: Intermediário

O segundo caso tem como objetivo realizar um treinamento de um modelo utilizando o Sagemaker. O dataset utilizado foi o MNIST e o objetivo é de colocar os dez números em cluster. Dessa forma, foi utilizado o modelo K-Means do próprio Sagemaker.

Pré-requisitos:
- [Conta no AWS](https://aws.amazon.com/getting-started/guides/setup-environment/)
- [IAM role criada](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role-sagemaker-notebook.html)
- [SageMaker Notebook Instance]((https://docs.aws.amazon.com/sagemaker/latest/dg/howitworks-create-ws.html))
- [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)

Tendo os pré-requisitos, será necessário criar um notebook no Jupyter Notebook do Sagemaker e executar as células. O notebook se encontra na pasta "Intermediario" nesse repositório.

## Caso 3: Avançado

Para a realização do terceiro caso, foi criado um dataset, apenas como exemplo, com dados de residências e com os seus valores. O objetivo é de realizar a predição do valor das casas através das informações: Número de camas, número de banheiros, tamanho da casa e ano de construção. 

O modelo utilizado foi o Random Forest e no notebook criado o treinamento foi realizado de duas maneiras: treinamento convencional, utilizando a biblioteca do sklearn diretamente no notebook e o treinamento utilizando o modo de script do sagemaker.

Pré-requisitos:
- [Conta no AWS](https://aws.amazon.com/getting-started/guides/setup-environment/)
- [IAM role criada](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role-sagemaker-notebook.html)
- [SageMaker Notebook Instance]((https://docs.aws.amazon.com/sagemaker/latest/dg/howitworks-create-ws.html))
- [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)

Após isso, será necessário criar um notebook no Jupyter Notebook do SageMaker e executar as células. Na pasta 'Avancado', há um notebook pronto para ser executado no SageMaker. Dentro dessa pasta, há também outra pasta chamada 'scripts', que precisará ser incluída localmente na instância do Jupyter Notebook criada, pois essa pasta contém o script com o modelo implementado.

## Referências
Amazon Web Services (AWS). Tutorial: Criar automaticamente modelos de machine learning com Amazon SageMaker Autopilot. Disponível em: https://aws.amazon.com/pt/tutorials/machine-learning-tutorial-automatically-create-models/. Acesso em: 28 set. 2024.

Amazon Web Services (AWS). SageMaker Script Mode. Disponível em: https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-script-mode/sagemaker-script-mode.html. Acesso em: 28 set. 2024.

Amazon Web Services (AWS). Treinamento e previsão usando K-Means no Amazon SageMaker. Disponível em: https://docs.aws.amazon.com/sagemaker/latest/dg/k-means.html. Acesso em: 28 set. 2024.

AMAZON WEB SERVICES (AWS). Amazon SageMaker Examples - GitHub repository. Disponível em: https://github.com/aws/amazon-sagemaker-examples/tree/main. Acesso em: 28 set. 2024.