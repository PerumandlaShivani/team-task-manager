import os
from app import app, db

# Railway-specific startup
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    
    with app.app_context():
        # Create tables
        db.create_all()
        print("✅ Database tables created successfully")
        
        # Test database connection
        from sqlalchemy import text
        try:
            result = db.session.execute(text('SELECT 1'))
            print("✅ Database connection verified")
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
    
    print(f"🚀 Starting Team Task Manager on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
