import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        #Criação de uma lista com as 3 variaveis que vão ser utilizadas
        trabalhos = list(zip(startTime,endTime ,profit ))
		
		# ordena por hora de inicio
        trabalhos.sort(key=lambda x:x[0])
        
        n = len(trabalhos)
        
		# Cria uma matriz inicial com os trabalhos
        inicio = [trabalhos[i][0] for i in range(n) ]
        
        pd = [0 for _ in range(n)]
		
		#Pegando a matriz e lendo ela de cima para baixo, o lucro máximo do último, seria o seu próprio lucro, bottom up
        pd[n-1] = trabalhos[n-1][2]
        
        for i in range(n-2,-1,-1):
			#Encontra o primeiro indice da matriz onde o trabalho/job termina
            idx = bisect.bisect_left(inicio, trabalhos[i][1], i, n)
			
			#O pd recebe o valor max do idx
            pd[i] = max(pd[i+1], trabalhos[i][2]+ (pd[idx] if idx < n else 0) )
        
        return pd[0]