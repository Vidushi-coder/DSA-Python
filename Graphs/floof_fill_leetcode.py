from collections import deque
def flood_fill(image,sr,sc, color):
  original = image[sr][sc]

  if original == color:
    return image

  m=len(image)
  n=len(image[0])
  
  q = deque()
  q.append((sr,sc))

  image[sr][sc]=color
  directions = [(-1,0),(1,0),(0,1),(0,-1)]

  while q:
    r,c = q.popleft()

    for dr,dc in directions:
      nr = r+dr
      nc = c+dc

      if(0<=nr<m and 0<=nc<n and image[nr][nc]==original):
        image[nr][nc]=color
        q.append((nr,nc))

  return image

if __name__ == "__main__":
  image = [[1,1,1],[1,1,0],[1,0,1]]
  sr=1
  sc=1
  color = 2
  print(flood_fill(image,sr,sc, color))