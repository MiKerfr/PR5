const request = require('supertest');
const app = require('../app.py');

describe('GET /time', () => {
  it('should return non-zero unix time', async () => {
    const res = await request(app).get('/time');
    
    
    expect(res.statusCode).toEqual(200);
    
    
    expect(res.body).toHaveProperty('time');
    
    
    expect(res.body.time).not.toEqual(0);
    
    
    const currentTime = Math.floor(Date.now() / 1000);
    expect(res.body.time).toBeGreaterThan(currentTime - 100);
    expect(res.body.time).toBeLessThan(currentTime + 100);
  });
});
